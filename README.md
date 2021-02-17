
# wlc_acl_redirect
Script to create ACLs (Local Mode) Posture and WebAuth Redirect to Cisco WLC running AirOS.
We need these ACLs when integration with ISE and using Posture and WebAuth (Guest Portal).

# Requires:
- Python (tested on Python 3.8.6 for Windows)

# Usage:
1) Download this repository or copy all of the content from wlc_acl_ise.py file into a python file
2) Run wlc_acl_ise.py
3) Inform how many PSN you have (ex: 2)
4) Inform how many remediation servers you have (ex: 1)
5) Inform IP address of each PSN and Remediation Server (Ex: 10.1.1.1)
6) A .txt file will be generated with the ACLs
7) Copy the ACLs to the WLC (CLI)

![Output](https://raw.githubusercontent.com/andreirapuru/wlc_acl_redirect/main/wlc_acl_redirect.png)

# Use case:
- Create acls (local mode) to be applied on Cisco WLC running AirOS, when deploying ISE and using Posture and WebAuth (Guest Portal).

# Getting Help:
- If you are having trouble or need help, create an issue [here](https://github.com/andreirapuru/wlc_acl_redirect/issues)

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/andreirapuru/wlc_acl_redirect)
