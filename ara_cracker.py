Skip to content

Learn Git and GitHub without any code!

Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.

Read the guide

cr4ck3r1/fb

CodeIssuesPull requestsActionsProjectsWikiSecurityInsights

 main 

fb/lazytool.py

cr4ck3r1 Update lazytool.py

 1 contributor

3799 lines (3727 sloc)  334 KB

RawBlame

 

#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsidhsgw82oo3e8ehensnsosbsue9e8272hsnsjs8ssjwne8s7w7wwjwiw8w8w82wjwjwjwiw8w8wiwjejjwiw88w7w8w7#kakajksksjsjseu3jend7dnsid

