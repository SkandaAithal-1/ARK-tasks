#!/usr/bin/env python3
import rospy
import std_msgs
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

pub1 = rospy.Publisher('/guess', Image, queue_size=10)
bridge = CvBridge()

def strategy():
	global imgMsg
	imheight=512
	imwidth=512
	b,g,r=0,1,2
	imgMsg=None
	rospy.init_node('player_node')
	rospy.Subscriber("/result", Image, guessCallback)
	rospy.sleep(1)
	guess = np.zeros((imheight,imwidth,3), dtype=np.uint8)
	track = np.zeros((imheight,imwidth,6))
	guess+=127
	track[:,:,1]+=255
	track[:,:,3]+=255
	track[:,:,5]+=255
	msg=bridge.cv2_to_imgmsg(guess, 'bgr8')
	pub1.publish(msg)
	while not rospy.is_shutdown():
		while imgMsg is None:
			pass
		imgMsg=imgMsg.astype(int)
		print(imgMsg)
		'''for i in range(imheight):
			for j in range(imwidth):
				if(imgMsg[i,j,g]==0):
					track[i,j,0]=guess[i,j,r]
					guess[i,j,r]=int((track[i,j,0]+track[i,j,1])/2)
				elif(imgMsg[i,j,g]==255):
					track[i,j,1]=guess[i,j,r]
					guess[i,j,r]=int((track[i,j,0]+track[i,j,1])/2)
				if(imgMsg[i,j,b]==0):
					track[i,j,2]=guess[i,j,g]
					guess[i,j,g]=int((track[i,j,2]+track[i,j,3])/2)
				elif(imgMsg[i,j,b]==255):
					track[i,j,3]=guess[i,j,g]
					guess[i,j,g]=int((track[i,j,2]+track[i,j,3])/2)
				if(imgMsg[i,j,r]==0):
					track[i,j,4]=guess[i,j,b]
					guess[i,j,b]=int((track[i,j,4]+track[i,j,5])/2)
				elif(imgMsg[i,j,r]==255):
					track[i,j,5]=guess[i,j,b]
					guess[i,j,b]=int((track[i,j,4]+track[i,j,5])/2)'''
		g0=np.where(imgMsg[:,:,g]==0)
		g1=np.where(imgMsg[:,:,g]==255)
		b0=np.where(imgMsg[:,:,b]==0)
		b1=np.where(imgMsg[:,:,b]==255)
		r0=np.where(imgMsg[:,:,r]==0)
		r1=np.where(imgMsg[:,:,r]==255)
		
		for (j,i) in zip(*g0[::-1]):
			track[i,j,0]=guess[i,j,r]
			guess[i,j,r]=((track[i,j,0]+track[i,j,1])/2)
		for (j,i) in zip(*g1[::-1]):
			track[i,j,1]=guess[i,j,r]
			guess[i,j,r]=((track[i,j,0]+track[i,j,1])/2)
		for (j,i) in zip(*b0[::-1]):
			track[i,j,2]=guess[i,j,g]
			guess[i,j,g]=int((track[i,j,2]+track[i,j,3])/2)
		for (j,i) in zip(*b1[::-1]):
			track[i,j,3]=guess[i,j,g]
			guess[i,j,g]=int((track[i,j,2]+track[i,j,3])/2)
		for (j,i) in zip(*r0[::-1]):
			track[i,j,4]=guess[i,j,b]
			guess[i,j,b]=int((track[i,j,4]+track[i,j,5])/2)
		for (j,i) in zip(*r1[::-1]):
			track[i,j,5]=guess[i,j,b]
			guess[i,j,b]=int((track[i,j,4]+track[i,j,5])/2)
					
		msg=bridge.cv2_to_imgmsg(guess, "bgr8")
		imgMsg=None
		pub1.publish(msg)
		while imgMsg is None:
			pass	
		rospy.sleep(0.2)
				
					
	
	
			
def guessCallback(data):
	global imgMsg
	imgMsg = bridge.imgmsg_to_cv2(data, "bgr8")
	
if __name__ == '__main__':
	try:
		strategy()
	except rospy.ROSInterruptException:
		pass












