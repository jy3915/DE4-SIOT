import oss2

auth = oss2.Auth('25704006', 'ab8c9ccc96d3621e529d18545d8ff65d')
# Access key ID and Access key secret

bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'SIOT')
# Endpoint url based on location and name of storage space.

bucket.create_bucket(oss2.models.BUCKET_ACL_PRIVATE)
# Set storage space as private
