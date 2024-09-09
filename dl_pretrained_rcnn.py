import kagglehub

# Download latest version
path = kagglehub.model_download("google/faster-rcnn-inception-resnet-v2/tensorFlow1/faster-rcnn-openimages-v4-inception-resnet-v2")

print("Path to model files:", path)