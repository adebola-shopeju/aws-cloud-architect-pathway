# W1-D3 Journal — IAM & AWS CLI
Date: 10 June 2026

## What I learned today
IAM is the control panel that manages permissions and access through groups. When you create a group, every member inherits all the access assigned to that group. To give multiple department heads the same access to a particular resource, the best practice is to create a new group, add the users, and they will all share consistent access this avoids inconsistency, mistakes, omissions, and wasted time.

Additionally, we treat the root account as sacred we never use it to create anything. The more the root account is used, the more vulnerable it becomes to corruption, theft, or hacking. So the safest approach is to keep it locked away and grant no one access to it.

I also learned the difference between users and roles. A user is a permanent staff member who can access designated resources. A role, on the other hand, is a temporary identity that follows the principle of least privilege. Roles can also be assigned to machines.

## What was difficult and why
Grasping the distinction between users and roles was challenging at first especially understanding that roles can be temporary and can also be attached to machines, not just people. It took some time to move beyond the intuitive idea that only human users get permissions, and to see how roles enable more secure, just in time access.

## One thing I want to explore further
I want to explore how roles are assigned to machines (e.g., EC2 instances) and how automated systems assume roles without human intervention. Understanding real world examples of least privilege in action would help solidify the concept.
