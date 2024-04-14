# YellowTech API Infrastructure Outage - Incident Report

![Oops](https://cdc.govt.nz/wp-content/uploads/2019/06/technical-difficulties-400x250.png)

## Summary

On July 17, 2024, between 8:12 AM and 9:45 AM GMT, YellowTech's internal customer dashboard experienced a serious case of the Mondays, with performance taking an unexpected coffee break. Approximately 50% of users trying to access critical functionalities were caught in the slow lane due to a mischievous misconfiguration in our caching layer.

## Root Cause

The incident was triggered by a recent update to the caching configuration, which introduced a misconfiguration that caused excessive cache misses. This overwhelmed our backend servers and led to degraded performance for dashboard users.

## Resolution and Recovery

Upon detection of the issue at 8:12 AM GMT, our team immediately sprang into action, determined to restore order and banish the Monday blues. By 9:20 AM, we unmasked the misconfigured caching layer as the root cause and swiftly reverted the settings to their stable state. We performed controlled restarts of affected services, and by 9:45 AM, dashboard performance was fully restored.

## Timeline (GMT)

- **8:12 AM:** Monitoring systems detected performance degradation; alarms sounded, signaling the start of our troubleshooting mission.
- **8:15 AM:** Engineering team assembled and began investigating, diving deep into the application layer for clues.
- **8:30 AM:** Focused investigation led us closer to the culprit, like detectives unraveling a mystery.
- **9:00 AM:** Incident escalated to senior team for resolution; urgent meetings and brainstorming sessions ensued.
- **9:20 AM:** Misconfigured caching layer identified and swiftly corrected, bringing clarity to the chaos.
- **9:45 AM:** Dashboard performance restored to normal; sighs of relief echoed through YellowTech HQ.

## Corrective and Preventative Measures

To prevent similar incidents in the future and enhance system resilience, we have taken the following actions:

- **Enhanced Change Management:** All configuration changes will undergo rigorous testing and review before deployment, ensuring no mischievous misconfigurations slip through the cracks.
- **Improved Monitoring:** Enhanced monitoring systems to proactively detect and alert us of performance anomalies before they disrupt our Monday mornings.
- **Caching Configuration Review:** Conducted a comprehensive review of all caching configurations to ensure alignment with best practices and performance requirements.

## Conclusion

We apologize for any inconvenience caused by this incident and appreciate your understanding. Our team is committed to continuously improving our systems and ensuring the reliability of our services.

For further inquiries or assistance, please contact the YellowTech API Infrastructure Team.