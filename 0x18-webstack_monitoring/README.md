 Webstack monitoring
====================
Why is Monitoring Needed?: Monitoring helps detect issues before they impact users, ensures systems are performing as expected, and provides data for troubleshooting and optimizing performance.
Two Main Areas of Monitoring:
Application Monitoring: Observes the behavior and performance of running software, checking for errors, performance bottlenecks, and overall health.
Server Monitoring: Tracks the health and performance of servers, including metrics like CPU usage, memory usage, disk space, and network traffic.
Access Logs: Logs that record every request made to the server, including the URL requested, response status, and IP address of the requester.
Error Logs: Logs that record errors or issues encountered by the server, which can help in diagnosing and troubleshooting problems.
2. Resources
What is Server Monitoring: Learn about the tools and techniques for monitoring server health, such as CPU and memory usage.
What is Application Monitoring: Understand how to monitor application performance, detect anomalies, and ensure expected behavior.
System Monitoring by Google: Review how Google approaches system monitoring and the tools they use.
Nginx Logging and Monitoring: Study how to configure and use Nginx logs for monitoring server performance.
3. Setup and Configuration
Access and Error Logs:

Nginx Configuration: Ensure that your Nginx server is set up to generate both access and error logs.
Log Locations: Typically, access logs are found at /var/log/nginx/access.log and error logs at /var/log/nginx/error.log.
Monitoring Tools:

For Application Monitoring: Tools like Prometheus, Grafana, or New Relic can help monitor application performance.
For Server Monitoring: Tools like Nagios, Zabbix, or Munin are useful for monitoring server health.
4. Implement Scripts
Bash Scripts: Write Bash scripts to automate monitoring tasks. Ensure they:
Start with #!/usr/bin/env bash
Include a comment on the second line explaining the script's purpose
Pass Shellcheck without errors
Are executable
5. Documentation
README.md: Include a detailed README file at the root of your project folder. This should explain the purpose of your scripts, how to use them, and any other relevant information.
6. Testing
On Ubuntu 16.04 LTS: Make sure your scripts are tested and functional on Ubuntu 16.04 LTS, as this is the environment your scripts will be executed in.
