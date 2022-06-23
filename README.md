# 작품 개요
> - 임베디드 시스템에서 구동되는 다양한 어플리케이션이 많은 관심을 보이며, 특히 CPU 및 GPU를 갖는 Nvidia사에서 생산판매하고 있는 Jetson 보드가 가장 일반적으로 사용되고 있습니다.
> - 때문에 GPU가 설치되어 있어 고성능 AI 어플리케이션의 구동이 가능한 Jetson 보드와 라즈베리파이를 사용하여 로봇 제어기술인 ROS를 사용하여 AI와 ROS를 결합한 작품을 개발하고자 합니다.

# 1. 블록도
> ![image](https://user-images.githubusercontent.com/103561996/175265425-872dd966-ef0f-4bd5-84bd-4c4ba31b4091.png)
> ## 수정사항 및 주차별 블록도
> https://github.com/mhk0904/Capstone-Design/tree/main/%EC%A3%BC%EC%B0%A8%EB%B3%84ROS%EB%B8%94%EB%A1%9D%EB%8F%84

# 2. 개발 내용 
> ### Deep learning을 사용한 동작 인식 및 ROS상에서 topic을 기반으로 분산 제어를 구현하는 기술의 개발
> - jetson nano에서 Ros를사용하여 raspberry pi로 데이터를 송신합니다.
> - opencv와 mediapipe를 사용하여 카메라로 영상검출을 하여 동작을 따라하는 로봇핸드를 조작하고
> - gtts를 사용하여 마이크에서 음성인식을 통한 추가적인 동작을 수행할수있도록 제작하였습니다.
> > [https://github.com/mhk0904/Capstone-Design/blob/774a24c460d85b6314ba489e317e031863bef391/Prerequisite](https://github.com/mhk0904/Capstone-Design/blob/main/Prerequisite.md)


## 3. 개발 환경
> ### Jetson nano에 연결된 카메라와 마이크로부터 영상검출을 하고, 검출한 데이터를 topic을 기반으로 Ros를 통해 publish하여 라즈베리파이에서 로봇핸드를 동작시킵니다.
>  - Jetson nano에서 Ros Melodic을 사용하여 cam node에서 HandPosition Topic을 hand control node로 publish합니다
>  - stt node에서 Ros Melodic을 사용하여 sound Topic으로 hand control node로 publish합니다
>  - Raspberry Pi의 hand control node는 cam node에서 subscribe한 모션검출결과와 stt node에서 subscribe한 결과를 수행시켜 로봇핸드를 동작시킵니다.
> > [https://github.com/mhk0904/Capstone-Design/blob/774a24c460d85b6314ba489e317e031863bef391/Prerequisite](https://github.com/mhk0904/Capstone-Design/blob/main/Prerequisite.md)
> > 
# 4. 소스 코드
> https://github.com/mhk0904/Capstone-Design/tree/main/Code
