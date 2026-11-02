# Security Review Checklist

- trust boundary is named
- auth and authorization path checked
- auth abuse throttling checked where unauthenticated repetition is possible
- enumeration risk checked on login, signup, and recovery paths where relevant
- validation and encoding path checked
- secrets and logs checked
- client-visible error exposure checked
- browser hardening headers checked when authenticated content is served
- abuse or rate-limit exposure checked
- severity and remediation owner recorded
