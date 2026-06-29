# W4-D1 Journal — Amazon S3 Buckets & Objects
**Date:** 29 June 2026

## What I learned today
- S3 is object storage — buckets are containers, objects are files, 
  keys are the name tags
- Bucket names must be globally unique because they become part of a URL
- S3 has no real folders — just flat storage with long key names
- Storage classes: Standard, Intelligent-Tiering, Glacier, Deep Archive
- Block all public access protects buckets from internet strangers

## What I built
- Created bucket `week4-adebola-0001` via console
- Created bucket `week4-cli-adebola-1782764912` via CLI
- Uploaded, downloaded, deleted and re-uploaded objects
- Ran full CLI cycle: mb, cp, ls, cp download

## Errors I hit and fixed
- `s3:CreateBucket` permission missing from adebola_dev → fixed by 
  root attaching AmazonS3FullAccess
- adebola_dev cannot attach its own policies → only root can do that
- AccessDenied on object URL → expected, bucket has public access blocked

## One thing to explore further
Presigned URLs — temporary links that give time-limited access to 
private objects without making the bucket public

## Confidence sentence
I can now create S3 buckets and manage objects using both the console 
and the CLI.