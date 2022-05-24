# 1. 개발 내용
> jetson nano에서 Ros를사용하여 raspberry pi로 데이터를 송신합니다. opencv와 mediapipe를 사용하여 카메라로 영상검출을 하여 동작을 따라하는 로봇핸드를 조작하고, gtts를 사용하여 마이크에서 음성인식을 통한 추가적인 동작을 수행할수있도록 제작하였습니다.

## 동작 설명
> ### Jetson nano에 연결된 카메라와 마이크로부터 Ros를 사용하여 라즈베리파이로 publish하여 로봇핸드를 동작시킵니다.
>  - Jetson nano에서 Ros Melodic을 사용하여 cam node에서 핸드포지션 토픽을 hand control node로 publish합니다
>  - stt node에서 Ros Melodic을 사용하여 sound 토픽으로 hand control node로 publish합니다
>  - 라즈베리파이에서 Ros Melodic을 사용하여 hand control node는 cam node에서 subscribe한 모션검출결과와 stt노드에서 subscribe한 결과를 수행시켜 로봇핸드를 동작시킵니다.
``` 영제바보 ```
# 2. 블록도
![image](https://user-images.githubusercontent.com/103232858/168215610-c59157b0-c028-4731-8eed-6bf84b7fb56c.png)
# 3. 사용된 패키지
Opencv (4.5.5V)
Mediapipe (0.8.5V)
ros_vosk
# 4. 수정 사항 및 개선방향
라즈베리파이에서 파이카메라와 마이크를 사용하여 로봇핸드를 동작시키려 했지만 jetson nano 보드에서 카메라와 마이크를 사용해 라즈베리파이로 publish하도록 변경하였습니다.
