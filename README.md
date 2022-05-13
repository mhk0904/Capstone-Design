# 1. 블록도
![image](https://user-images.githubusercontent.com/103232858/168215610-c59157b0-c028-4731-8eed-6bf84b7fb56c.png)
# 2. 개발 내용
Jetson nano에 연결된 카메라와 마이크로부터 opencv기반의 패키지로부터 Ros를 사용하여 라즈베리파이로 publish하여 로봇핸드를 동작시킵니다.
- Jetson nano에서 Ros Melodic을 사용하여 cam node에서 핸드포지션 토픽을 hand control node로 publish합니다
- stt node에서 Ros Melodic을 사용하여 sound 토픽으로 hand control node로 publish합니다
- 라즈베리파이에서 Ros Melodic을 사용하여 hand control node는 cam node에서 subscribe한 모션검출결과와 stt노드에서 subscribe한 결과를 수행시켜 로봇핸드를 동작시킵니다.
# 3. 사용된 패키지
Opencv (4.5.5V)
Mediapipe (0.8.5V)
ros_vosk
# 4. 수정 사항 및 개선방향
라즈베리파이에서 파이카메라와 마이크를 사용하여 로봇핸드를 동작시키려 했지만 jetson nano 보드에서 카메라와 마이크를 사용해 라즈베리파이로 publish하도록 변경하였습니다.
