# wlc_acl_redirect
Script to create ACLs Posture and WebAuth Redirect to Cisco WLC running AirOS.

Requires:
- python (tested on python 3.8.6 Windows)

Usage:
1) Inform how many PSN you have
2) Inform how many remediation servers you have
3) Inform IP address of each PSN and Remediation Server (Ex: 10.1.1.1)
3) Run wlc_acl_ise.py

Use case:
- create acls to be applied on Cisco WLC running AirOS, when deploying ISE.
