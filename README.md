# Real  time Log Analysis and Alerting : 
# Apache NiFi with FastAPI Project

## Overview

This project demonstrates the integration of Apache NiFi, a robust data processing platform, with FastAPI, a modern web framework for building APIs. The project showcases the extraction, processing, and transmission of data between NiFi and FastAPI, facilitating seamless data handling and analysis.

## Features

- **NiFi Workflow:** Configures a data flow in Apache NiFi for data extraction and transformation.
- **ExtractGrok Processor:** Extracts specific data patterns from log files.
- **InvokeHTTP Processor:** Sends extracted data to a FastAPI endpoint.
- **FastAPI Endpoint:** Receives and processes data sent by NiFi.

## Prerequisites

- Apache NiFi installed and configured.
- FastAPI environment set up and running.

## Usage

1. **NiFi Setup:**
   - Import the NiFi flow template provided in the `NiFi_Flow_Template.xml` file.
   - Adjust configurations according to your environment.

2. **FastAPI Setup:**
   - Run the FastAPI application.
   - Ensure the endpoint for NiFi data reception is operational.

3. **NiFi Workflow Execution:**
   - Start the NiFi flow to extract and transmit data to FastAPI.

## Directory Structure

- `logs_fastapiAlert_MehdiTouil.xml`: Apache NiFi flow template file.
- `FastAPI/`: FastAPI application code and configurations.

## Resources

- [Apache NiFi Documentation](https://nifi.apache.org/docs.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
## screenshots
![Apache Nifi Template 1](https://raw.githubusercontent.com/mehdi-touil/Real-time-Log-Analysis-and-Alerting/487dea73ca41ee59c302a5212cdb60ba7b8aaead/Screenchots/Apache%20Nifi%20Template%201.png)
![Apache Nifi Template 2](https://raw.githubusercontent.com/mehdi-touil/Real-time-Log-Analysis-and-Alerting/487dea73ca41ee59c302a5212cdb60ba7b8aaead/Screenchots/Apache%20nifi%20Template%202.png)
![FastAPI Received Alert From Apache NiFi](https://raw.githubusercontent.com/mehdi-touil/Real-time-Log-Analysis-and-Alerting/487dea73ca41ee59c302a5212cdb60ba7b8aaead/Screenchots/FastApi%20Received%20Alert%20From%20Apache%20Nifi.png)
## Contributors

- [Mehdi Touil](https://github.com/mehdi-touil)

## License

This project is licensed under the [MIT License](LICENSE).
