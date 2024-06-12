import json
from frictionless import Package, Report

def validate_package(package_path, output_path):
    # Load the data package
    package = Package(package_path)

    # Validate the package
    report = package.validate()
    print(report)
    # Prepare the results dictionary
    results = {        
        "report": report.to_dict(),
        "errorsummary": []
    }

    # Check if validation passed
    if report.valid:
        print("Data package is valid.")
    else:
        print("Data package has validation errors.")
        for error in report.flatten(["rowNumber", "fieldNumber", "fieldName", "message", "type"]):
            print(f"Row: {error[0]}, fieldNumber: {error[1]}, fieldName: {error[2]}, Message: {error[3]}, Type: {error[4]}")
            # Append each error to the results dictionary
            results["errorsummary"].append({
                "rowNumber": error[0],
                "fieldNumber": error[1],
                "fieldName": error[2],
                "message": error[3],
                "type": error[4]
            })

  

    # Write the results to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    package_path = "datapackage.json"
    output_path = "validation_report.json"
    validate_package(package_path, output_path)
