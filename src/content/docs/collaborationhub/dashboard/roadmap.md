---
title: Roadmap
---

#### Objective: Ensure Efficient and Accurate Processing of FHIR Submissions

#### Job to Be Done:
- Track the status of all submissions from SCNs in real-time.
- Provide a visual representation of submission status.
- Allow detailed views of individual submissions.

#### Widgets to Provide:

1. **Total Submissions**
   - **Widget Type**: Counter
   - **Purpose**: Display the total number of FHIR documents received.
   - **Details**: Shows a dynamic count of all submissions to date.

2. **Pending Submissions**
   - **Widget Type**: Counter
   - **Purpose**: Number of submissions currently being processed.
   - **Details**: Updated in real-time to reflect the current number of pending submissions.

3. **Accepted Submissions**
   - **Widget Type**: Counter
   - **Purpose**: Number of submissions accepted.
   - **Details**: Displays the count of all accepted submissions to date.

4. **Rejected Submissions**
   - **Widget Type**: Counter
   - **Purpose**: Number of submissions rejected.
   - **Details**: Shows the current count of rejected submissions.

5. **Submission Status Overview**
   - **Widget Type**: Pie Chart
   - **Purpose**: Display the proportion of submissions in different statuses (e.g., Pending, Accepted, Rejected).
   - **Details**: Interactive segments to drill down into specific statuses.

6. **Submission Status Table with Filtering and Pivot Capabilities**
   - **Widget Type**: Table
   - **Purpose**: List all submissions with detailed information such as Submission ID, SCN Name, Date Submitted, Status, and Errors (if any).
   - **Details**: Sortable and searchable with advanced filters for status, date range, SCN, and pivot table functionality to customize views.

7. **Submission Detail View**
   - **Widget Type**: Modal / Popup
   - **Purpose**: Provide a detailed view of individual submissions when selected from the table or chart.
   - **Details**: Include information such as full submission data, error details, processing logs, and history of status changes.

8. **Recent Submissions List**
   - **Widget Type**: List / Card View
   - **Purpose**: Display a list of the most recent submissions with key details.
   - **Details**: Quick access to the latest submissions and their status.

9. **Submission Error Summary**
   - **Widget Type**: Bar Chart / Histogram
   - **Purpose**: Summarize and categorize common errors found in submissions.
   - **Details**: Drill down into specific error types for more detailed analysis.

---

#### Objective: Improve Data Quality and Error Resolution

#### Job to Be Done:
- Identify and resolve errors in FHIR submissions promptly.
- Provide detailed error reports and logs.
- Track common errors and trends over time.

#### Widgets to Provide:

1. **Error Summary**
   - **Widget Type**: Bar Chart / Pie Chart
   - **Purpose**: Display the distribution and frequency of different types of errors.
   - **Details**: Visual representation to quickly identify the most common errors.

2. **Detailed Error Log**
   - **Widget Type**: Table
   - **Purpose**: List all errors with detailed information such as Submission ID, SCN Name, Date, Error Type, and Error Description.
   - **Details**: Sortable and searchable with filtering options for specific error types, dates, or SCNs.

3. **Submission Error Rate**
   - **Widget Type**: KPI Card / Counter
   - **Purpose**: Display the percentage of submissions with errors.
   - **Details**: Provides an at-a-glance understanding of data quality and helps set targets for improvement.

4. **Top 5 Frequent Errors**
   - **Widget Type**: List / Bar Chart
   - **Purpose**: Highlight the most frequent errors encountered in submissions.
   - **Details**: Focuses attention on the most critical issues that need resolution.

5. **SCN Error Comparison**
   - **Widget Type**: Comparative Bar Chart / Heatmap
   - **Purpose**: Compare error rates and types across different SCNs.
   - **Details**: Identifies SCNs with higher error rates and helps target support and training efforts.

6. **Interactive Error Drill-Down**
   - **Widget Type**: Table
   - **Purpose**: Allow users to drill down from summary charts into detailed error data.
   - **Details**: Provides a deeper understanding of specific errors and their contexts.

---

#### Objective: Enhance Communication and Coordination

#### Job to Be Done:
- Set up real-time notifications for submission status changes.
- Facilitate better communication within the QE team and with SCNs.
- Keep SCNs informed about the status of their submissions.

#### Widgets to Provide:

1. **Real-Time Notification Panel**
   - **Widget Type**: Notification Panel / Alert Box
   - **Purpose**: Display real-time alerts for submission status changes.
   - **Details**: Includes notifications for status updates such as Pending, Accepted, Rejected, and Error Occurred. Customizable alert settings based on user preferences.

2. **SCN Communication Hub**
   - **Widget Type**: Messaging Interface / Communication Portal
   - **Purpose**: Enable direct communication between the QE team and SCNs.
   - **Details**: Provides a platform for sending and receiving messages, sharing updates, and resolving issues collaboratively.

3. **Submission Status Email Alerts**
   - **Widget Type**: Email Notification System
   - **Purpose**: Automatically send email updates to SCNs about the status of their submissions.
   - **Details**: Configurable to send alerts for different statuses and changes, ensuring SCNs are always informed.

4. **SCN Status Dashboard**
   - **Widget Type**: Personalized Dashboard for SCNs
   - **Purpose**: Allow SCNs to monitor the status of their submissions in real-time.
   - **Details**: Displays submission status, error notifications, and any required actions. Interactive and user-friendly interface.

5. **Collaborative Issue Tracker**
   - **Widget Type**: Issue Tracking System
   - **Purpose**: Track and manage issues or queries raised by SCNs.
   - **Details**: Allows SCNs to report problems and QE team to provide updates and resolutions. Tracks the progress and status of each issue.

6. **SCN Feedback Form**
   - **Widget Type**: Feedback Form / Survey
   - **Purpose**: Collect feedback from SCNs about the submission process and communication effectiveness.
   - **Details**: Enables continuous improvement based on SCN inputs and suggestions.

7. **Real-Time Chat Support**
   - **Widget Type**: Live Chat Interface
   - **Purpose**: Provide instant support and answers to SCNs regarding their submissions.
   - **Details**: Enables real-time conversations between SCNs and QE team members for quick resolution of queries and issues.

---

#### Objective: Improve Data Quality and Error Resolution (Duplicate Section)

#### Job to Be Done:
- Identify and resolve errors in FHIR submissions promptly.
- Provide detailed error reports and logs.
- Track common errors and trends over time.

#### Widgets to Provide:

1. **Error Summary**
   - **Widget Type**: Bar Chart / Pie Chart
   - **Purpose**: Display the distribution and frequency of different types of errors.
   - **Details**: Visual representation to quickly identify the most common errors.

2. **Detailed Error Log**
   - **Widget Type**: Table
   - **Purpose**: List all errors with detailed information such as Submission ID, SCN Name, Date, Error Type, and Error Description.
   - **Details**: Sortable and searchable with filtering options for specific error types, dates, or SCNs.

3. **Submission Error Rate**
   - **Widget Type**: KPI Card / Counter
   - **Purpose**: Display the percentage of submissions with errors.
   - **Details**: Provides an understanding of data quality and helps set targets for improvement.

4. **Top 5 Frequent Errors**
   - **Widget Type**: List / Bar Chart
   - **Purpose**: Highlight the most frequent errors encountered in submissions.
   - **Details**: Focuses attention on the most critical issues that need resolution.

5. **SCN Error Comparison**
   - **Widget Type**: Comparative Bar Chart / Heatmap
   - **Purpose**: Compare error rates and types across different SCNs.
   - **Details**: Identifies SCNs with higher error rates and helps target support and training efforts.

6. **Interactive Error Drill-Down**
   - **Widget Type**: Table
   - **Purpose**: Allow users to drill down from summary charts into detailed error data.
   - **Details**: Provides a deeper understanding of specific errors and their contexts.

7. **Recent Error Notifications**
   - **Widget Type**: Notification Panel / Alert Box
   - **Purpose**: Provide real-time alerts for newly identified errors.
   - **Details**: Ensures prompt attention and action on new issues as they arise.