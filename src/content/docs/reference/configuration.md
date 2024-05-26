---
title: Configuration Management with Environment Variables
description: How TechBD applications should be configured for multiple deployment environments
---

In Spring Boot, properties can be managed using various sources such as properties files, YAML files, and environment variables. This guide explains how to use `application.properties` and `application.yml` files in conjunction with environment variables to manage configuration properties in Java code using the `@Value` annotation. Additionally, it covers how properties can be overridden via HTTP headers or query parameters in REST Controllers, the importance of documenting property metadata, and best practices for using `@Value` annotations.

## Properties Files

### application.properties

Spring Boot allows you to define properties in the `application.properties` file located in the `src/main/resources` directory.

Example:

```properties
# application.properties
my.property=valueFromPropertiesFile
```

### application.yml

Alternatively, you can use the `application.yml` file for defining properties.

Example:

```yaml
# application.yml
my:
  property: valueFromYamlFile
```

## Using @Value Annotation

You can inject these properties into your Spring components using the `@Value` annotation.

Example:

```java
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class MyComponent {

    @Value("${my.property}")
    private String myProperty;

    public String getMyProperty() {
        return myProperty;
    }
}
```

### Best Practice: Using @Value in @Configuration Classes

While `@Value` annotations can be used without `@Configuration` annotations, if the same property is used in multiple places in the code, it is better and more type-safe to define the `@Value` once in a `@Configuration` class and then use that injected class in different places in custom code.

Example:

1. **Define properties in a configuration class**:

    ```java
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.context.annotation.Configuration;

    @Configuration
    public class MyConfig {

        @Value("${my.property}")
        private String myProperty;

        public String getMyProperty() {
            return myProperty;
        }
    }
    ```

2. **Use the configuration class in other components**:

    ```java
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Component;

    @Component
    public class MyComponent {

        private final MyConfig myConfig;

        @Autowired
        public MyComponent(MyConfig myConfig) {
            this.myConfig = myConfig;
        }

        public String getProperty() {
            return myConfig.getMyProperty();
        }
    }
    ```

This approach enhances type safety and centralizes the configuration properties, making it easier to manage and update them.

## Overriding Properties

### Command Line Arguments

Properties defined in `application.properties` or `application.yml` can be overridden using command line arguments.

Example:

```sh
java -jar myapp.jar --my.property=overriddenValueFromCLI
```

Or using the `-D` flag:

```sh
java -Dmy.property=overriddenValueFromCLI -jar myapp.jar
```

### Environment Variables

The preferred method for overriding properties, especially for secrets and environment-specific configurations, is using environment variables.

Example:

```sh
export MY_PROPERTY=overriddenValueFromEnv
```

To use environment variables in your properties file, you can define them with a default value:

#### application.properties

```properties
my.property=${MY_PROPERTY:defaultValueFromPropertiesFile}
```

#### application.yml

```yaml
my:
  property: ${MY_PROPERTY:defaultValueFromYamlFile}
```

In this setup, the environment variable `MY_PROPERTY` will override the value defined in the properties or YAML file.

## Automatic Property Resolution from Environment Variables

If a property is not defined in the `application.properties` or `application.yml` file, Spring Boot will automatically look for an environment variable following a specific naming convention to resolve the property.

### Naming Convention

Spring Boot maps environment variables to properties by replacing dots (`.`) in property names with underscores (`_`) and converting the property name to uppercase.

For example, if you have a property `my.property`, Spring Boot will look for an environment variable named `MY_PROPERTY`.

### Example

1. **Define a property in code**:

    ```java
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.stereotype.Component;

    @Component
    public class MyComponent {

        @Value("${my.property}")
        private String myProperty;

        public String getMyProperty() {
            return myProperty;
        }
    }
    ```

2. **Environment variable (if property is missing from files)**:

    ```sh
    export MY_PROPERTY=valueFromEnvIfMissingInProperties
    ```

In this example, if `my.property` is not defined in `application.properties` or `application.yml`, Spring Boot will automatically use the value from the environment variable `MY_PROPERTY`.

## Profiles

Spring Boot supports profiles to define different configurations for different environments. Profiles can be activated via environment variables or command line arguments.

### Defining Profiles

#### application-dev.properties

```properties
my.property=valueFromDevPropertiesFile
```

#### application-prod.properties

```properties
my.property=valueFromProdPropertiesFile
```

### Activating Profiles

Profiles can be activated by setting the `spring.profiles.active` environment variable or using command line arguments.

Example:

```sh
export SPRING_PROFILES_ACTIVE=prod
```

Or

```sh
java -jar myapp.jar --spring.profiles.active=prod
```

## Overriding Properties in REST Controllers

In addition to using properties files and environment variables, some properties can be overridden in REST Controllers via HTTP headers or query parameters. This can be useful for dynamic configuration and testing purposes.

### Example

1. **Controller Code**:

    ```java
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestHeader;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class MyController {

        @GetMapping("/config")
        public String getConfig(@RequestHeader(value = "X-My-Property", required = false) String headerValue,
                                @RequestParam(value = "myProperty", required = false) String queryValue) {
            String propertyValue = headerValue != null ? headerValue : (queryValue != null ? queryValue : "defaultValue");
            return "Property Value: " + propertyValue;
        }
    }
    ```

2. **OpenAPI Documentation**:

    The properties overridden via HTTP headers or query parameters should be documented in the OpenAPI (Swagger) documentation for better visibility and usage by API consumers.

    ```yaml
    paths:
      /config:
        get:
          summary: Retrieve configuration
          parameters:
            - name: X-My-Property
              in: header
              required: false
              schema:
                type: string
              description: Overrides my.property value from HTTP header
            - name: myProperty
              in: query
              required: false
              schema:
                type: string
              description: Overrides my.property value from query parameter
          responses:
            '200':
              description: successful operation
              content:
                application/json:
                  schema:
                    type: string
    ```

## Documenting Property Metadata

When creating a property, it's crucial to document its metadata and purpose for better maintainability and understanding. This documentation should include the property's name, default value, description, and any constraints.

### Example Metadata Documentation

#### application.properties

```properties
# Property: my.property
# Default Value: defaultValue
# Description: This property controls the behavior of XYZ component.
# Constraints: Must be a non-empty string.

my.property=defaultValue
```

#### application.yml

```yaml
# Property: my.property
# Default Value: defaultValue
# Description: This property controls the behavior of XYZ component.
# Constraints: Must be a non-empty string.

my:
  property: defaultValue
```

### Using @ConfigurationProperties for Grouping Related Properties

For grouping related properties, you can use the `@ConfigurationProperties` annotation along with a metadata file.

1. **Define the properties class**:

    ```java
    import org.springframework.boot.context.properties.ConfigurationProperties;
    import org.springframework.context.annotation.Configuration;

    @Configuration
    @ConfigurationProperties(prefix = "my")
    public class MyProperties {
        private String property;

        public String getProperty() {
            return property;
        }

        public void setProperty(String property) {
            this.property = property;
        }
    }
    ```

2. **Define the metadata file (`src/main/resources/META-INF/spring-configuration-metadata.json`)**:

    ```json
    {
      "properties": [
        {
          "name": "my.property",
          "type": "java.lang.String",
          "description": "This property controls the behavior of XYZ component.",
          "defaultValue": "defaultValue",
          "sourceType": "com.example.MyProperties"
        }
      ]
    }
    ```

By following these practices, you can ensure a flexible, secure, and well-documented configuration management strategy in your Spring Boot applications.
