---
title: Linux Sandbox
---

The following instructions are for setting up the code on a
[developer sandbox](https://en.wikipedia.org/wiki/Sandbox_(software_development))
("[dev sandbox](https://en.wikipedia.org/wiki/Sandbox_(software_development))"
or just
"[sandbox](https://en.wikipedia.org/wiki/Sandbox_(software_development))").

For dev sandboxes you should be able to use workstations or laptops that have:

- Modern i5 or i7 class CPUs (circa 2021 or later)
- 32GB RAM
- Any modern Linux Distro (or Windows Subsystem for Linux (WSL2) on Windows 11)
- [Amazon Correto Java 21](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/generic-linux-install.html)
  or above JDK and [Maven 3.9](https://maven.apache.org/download.cgi)+.

For Linux or MacOS use [pkgx](https://pkgx.sh/) and
[eget](https://github.com/zyedidia/eget/releases) to install dependencies. For
opinionated "batteries included" guidance see
[Strategy Coach Workspaces Host](https://github.com/strategy-coach/workspaces-host)
and then:

```bash
$ pkgx install sqlite.org duckdb.org
$ eget lovasoa/SQLpage --to=$HOME/.local/bin/sqlpage
```

This project uses Java 21+ and we prefer to use AWS Correto JVM because we will
deploy our Java services in AWS Lambda Serverless environments as well as in any
environments that support containers. If you're using
[Strategy Coach Workspaces Host](https://github.com/strategy-coach/workspaces-host)
opinionated developer experience sandbox you can use the following to setup
Java:

```bash
$ setup-java-amazon-corretto     # see https://github.com/strategy-coach/workspaces-host/blob/main/dot_config/fish/functions/setup-java-amazon-corretto.fish
```

### Setup the repository locally

If you're using
[Strategy Coach Workspaces](https://github.com/strategy-coach/workspaces)
opinionated developer repositories setup scripts you can use `ws-ensure.ts` or
"manually" clone the repo:

```bash
$ git clone https://github.com/qe-collaborative-services/1115-hub.git
$ cd 1115-hub/src/service/fhir-server-prime

$ mvn clean install      # download all dependencies
$ mvn wrapper:wrapper    # for integrating into IDEs and other CLI work (creates `.mvn` in project root)
```

Review
[`src/main/resources/application.properties`](https://github.com/qe-collaborative-services/1115-hub/blob/main/src/service/fhir-server-prime/src/main/resources/application.properties)
to configure the project.

- `shinnyDataLakeApiImpGuideProfileUri` property specifies the URI of the FHIR
  Implementation Guide profile.
- `shinnyDataLakeApiUri` property specifies the URI of the SHIN-NY Data Lake
  FHIR Submission endpoint.

### Run the code locally

```bash
$ mvn spring-boot:run -Dspring-boot.run.arguments="--server.port=8080 --server.host=localhost"
```
