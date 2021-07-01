import boto3

def get_number() -> str:
    
  #putting image in S3
  region = ""
  bucket_name = ""
  filename = "detected_plate.png"
  s3 = boto3.resource("s3")
  s3.Bucket(bucket_name).upload_file("detected_plate.png", "detected_plate.png")


  #calling Textract
  textract = boto3.client("textract", region_name = region)
  response = textract.detect_document_text(
      Document = {
        "S3Object" : {
          "Bucket" : bucket_name,
          "Name" : filename
         }
     }
  )
  
  
  number = response["Blocks"][1]["Text"].replace(" ", "")
  return number