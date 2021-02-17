
# wlc_acl_redirect
Script to create ACLs Posture and WebAuth Redirect to Cisco WLC running AirOS.
We need these ACLs when integration with ISE and using Posture and WebAuth (Guest Portal).

Requires:
- python (tested on python 3.8.6 for Windows)
- download this repository or copy all of the content from wlc_acl_ise.py file into a python file.


Usage:
1) Run wlc_acl_ise.py
2) Inform how many PSN you have (ex: 2)
3) Inform how many remediation servers you have (ex: 1)
4) Inform IP address of each PSN and Remediation Server (Ex: 10.1.1.1)
5) A .txt file will be generated with the ACL

Use case:
- Create acls to be applied on Cisco WLC running AirOS, when deploying ISE and using Posture and WebAuth (Guest Portal).

Getting Help:
- If you are having trouble or need help, create an issue here (https://github.com/andreirapuru/wlc_acl_redirect/issues)
