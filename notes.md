# Notes on Each Technique

## Error Level Analysis (ELA)
### Overview
- Due to JPEG being a lossy image format, there is error introduced at each resave
- JPEG algorithm uses 8x8 cells in the picture
- If the image is modified, each cell is no longer at the same error rate
### Implementation 
- User gives a JPEG image
- A copy of that image is made at a given quality rate (usually between 90-95%)
- The difference between each corresponding pixel is calculated via PIL `ImageChops.difference()`
- The max difference is calculated by running the result through the `max` function in python
- The scale for enhancement is determined by dividing 255 by the max difference calculated above
