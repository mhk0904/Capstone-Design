# 작품 개요
> - 임베디드 시스템에서 구동되는 다양한 어플리케이션이 많은 관심을 보이며, 특히 CPU 및 GPU를 갖는 Nvidia사에서 생산판매하고 있는 Jetson 보드가 가장 일반적으로 사용되고 있습니다.
> - 때문에 GPU가 설치되어 있어 고성능 AI 어플리케이션의 구동이 가능한 Jetson 보드와 라즈베리파이를 사용하여 로봇 제어기술인 ROS를 사용하여 AI와 ROS를 결합한 작품을 개발하고자 합니다.

# 1. 블록도
> ![image](https://user-images.githubusercontent.com/103232858/203708555-8035326a-73d7-435d-a170-69e8356ef4c9.png)
>
> ## 수정사항 및 주차별 블록도
> - https://github.com/mhk0904/Capstone-Design/tree/main/%EC%A3%BC%EC%B0%A8%EB%B3%84ROS%EB%B8%94%EB%A1%9D%EB%8F%84

# 2. 목적
> ### Deep learning을 사용한 동작 인식 및 ROS상에서 topic을 기반으로 분산 제어를 구현하는 기술 학습
>  - Jetson Xavier Nx에서 Ros Melodic을 사용하여 cam node에서 HandPosition Topic을 hand control node로 publish
>  - Raspberry Pi의 hand control node는 cam node에서 subscribe한 모션검출결과를 수행시켜 로봇핸드를 동작
>  - Jetson Xavier Nx에서 Ros Melodic을 사용하여 Flex Sensor의 데이터를 Flex node 로 Publish
>  - Raspberry pi의 Flex control node는 Flex node에서 subscribe한 각도로 로봇핸드를 동작


# 3 개발 내용 
> 1. Jetson Xavier Nx에 연결된 usb 카메라로 영상 인식 및 데이터 가공
>- Ros로 Raspberry pi4로 데이터 전송
>- Raspberry pi4에 연결한 Arduino Hat을 이용하여 Robot Hand 동작

> 2. Jetson Xavier Nx에 연결된 Arduino Mega2560의 Felx Sensor의 데이터 가공
>- Ros로 Raspberry pi4로 데이터 전송
>- Raspberry pi4에 연결한 Arduino Hat을 이용하여 Robot Hand 동작

# 4 개발 환경
>  - https://github.com/mhk0904/Capstone-Design/blob/main/Pre_requisite.md

# 5. 소스 코드
> - https://github.com/mhk0904/Capstone-Design/tree/main/Code

# 6. 작품 UCC
> # 작품 개요
> - 임베디드 시스템에서 구동되는 다양한 어플리케이션이 많은 관심을 보이며, 특히 CPU 및 GPU를 갖는 Nvidia사에서 생산판매하고 있는 Jetson 보드가 가장 일반적으로 사용되고 있습니다.
> - 때문에 GPU가 설치되어 있어 고성능 AI 어플리케이션의 구동이 가능한 Jetson 보드와 라즈베리파이를 사용하여 로봇 제어기술인 ROS를 사용하여 AI와 ROS를 결합한 작품을 개발하고자 합니다.

# 1. 블록도
> ![image](https://user-images.githubusercontent.com/103232858/203708555-8035326a-73d7-435d-a170-69e8356ef4c9.png)
>
> ## 수정사항 및 주차별 블록도
> - https://github.com/mhk0904/Capstone-Design/tree/main/%EC%A3%BC%EC%B0%A8%EB%B3%84ROS%EB%B8%94%EB%A1%9D%EB%8F%84

# 2. 목적
> ### Deep learning을 사용한 동작 인식 및 ROS상에서 topic을 기반으로 분산 제어를 구현하는 기술 학습
>  - Jetson Xavier Nx에서 Ros Melodic을 사용하여 cam node에서 HandPosition Topic을 hand control node로 publish
>  - Raspberry Pi의 hand control node는 cam node에서 subscribe한 모션검출결과를 수행시켜 로봇핸드를 동작
>  - Jetson Xavier Nx에서 Ros Melodic을 사용하여 Flex Sensor의 데이터를 Flex node 로 Publish
>  - Raspberry pi의 Flex control node는 Flex node에서 subscribe한 각도로 로봇핸드를 동작


# 3 개발 내용 
> 1. Jetson Xavier Nx에 연결된 usb 카메라로 영상 인식 및 데이터 가공
>- Ros로 Raspberry pi4로 데이터 전송
>- Raspberry pi4에 연결한 Arduino Hat을 이용하여 Robot Hand 동작

> 2. Jetson Xavier Nx에 연결된 Arduino Mega2560의 Felx Sensor의 데이터 가공
>- Ros로 Raspberry pi4로 데이터 전송
>- Raspberry pi4에 연결한 Arduino Hat을 이용하여 Robot Hand 동작

# 4 개발 환경
>  - https://github.com/mhk0904/Capstone-Design/blob/main/Pre_requisite.md

# 5. 소스 코드
> - https://github.com/mhk0904/Capstone-Design/tree/main/Code

# 6. 작품 UCC
> https://youtu.be/Yehc7ChCxdQ
