# Vehicle Counter Using Open-Cv 
A vehicle counting system, as you might have already inferred, is a system that counts vehicles on the road. Why would you want to build one? Why would you want to count vehicles on the road? Here are some reasons: 
[vehicle](https://opensourcelibs.com/lib/multitarget-tracker)
<img src="https://github.com/mohan-mathew/vehicle-counter-python/blob/main/0_iNYtQubKAtK0OGG5.png" alt="My cool logo"/>
*Traffic management and planning 

*Traffic control 

*Parking management 

*Advertising 
## Computer Vision Based Approach
Computer vision is concerned with the automatic extraction, analysis and understanding of useful information from a single image or a sequence of images. It involves the development of a theoretical and algorithmic basis to achieve automatic visual understanding. Vehicle detection and counting systems plays a major role in an intelligent transportation system, especially for traffic management system. Computer vision has also been applied for solving traffic and transportation problems. [There are multiple techniques to solve this problem. You can train a deep learning model for object detection or you can pick a pre-trained model and fine-tune it on your data. However, these are supervised learning approaches and they require labeled data to train the object detection model. Here we are going to use the unsupervised way of object detection in videos, i.e., is object detection without using any labeled data.] 

In this method we used an adaptive background subtraction technique to detect moving objects in a video and morphological operations. Then, vehicles were detected and counted by using a detector virtually located on the road. Finally, a blob tracking was done to match vehicles in the current frame and those in the previous frame.
