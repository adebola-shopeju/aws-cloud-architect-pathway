# W1-D7 Journal — Week 1 Wrap (Sunday)

## What I learned today
- Recorded my 2-minute intro video for my portfolio — first time putting
  my AWS goal and Week 1 progress into words on camera.
- Ran the full Linux command drill from memory (navigation, file
  creation, viewing/copying, permissions, cleanup) without notes.
- Reinforced file permissions: set config.yaml to 600 (rw-------,
  owner-only — like a locked diary) and server.log to 755
  (rwxr-xr-x — wider read/execute access).
- Recorded a voice memo explaining IAM least privilege, and connected
  it directly to the chmod work — least privilege isn't just an AWS
  concept, it's the same idea applied at the file-permission level.

## What was difficult, and why
- I accidentally typed `nano test data > server.log` instead of
  `echo "test data" > server.log`. Nano opened two file buffers
  ("test" and "data") and the redirect sent its screen output into
  server.log instead of the terminal, so my terminal looked frozen.
  I learned how to safely exit nano with Ctrl+X, and that `>` always
  overwrites a file completely — which let me fix it cleanly.
- I tried `rm week1-drill` to delete a folder and got
  "is a directory". I learned that plain `rm` only deletes files —
  deleting a directory (and its contents) needs `rm -r`.
- Both errors were unscripted, which made debugging them feel more
  real than a planned exercise would have.

## One thing I want to explore further
- Going into Week 2 (EC2, Security Groups, VPC deep dive), I want to
  understand how IAM least privilege actually gets applied to EC2
  instances — e.g. what an instance role/profile looks like in
  practice.

## Confidence statement
I have completed Week 1 of my AWS Cloud Architect journey and I am
ready for Week 2.
