import boto3, os

mys3 = boto3.client('s3')

try:
    results = mys3.list_buckets()
    print(results)
    output = ""
    for bucket in results['Buckets']:
        output = output + bucket['Name'] + "\n"
    return("<h1><font color=green>S3 Bucket List:</font></h1><br><br>" + output)
except:
    return("<h1><font color=red>Error!</font></h1><br><br>")