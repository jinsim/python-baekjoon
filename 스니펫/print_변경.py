"""
print() vs sys.stdout.write()
print()
- 줄바꿈하여 출력
- 메모리 적음
- 속도 느림
- 문자열이 아니더라도 출력 가능
sys.stdout.write()
- 줄바꿈없이 바로이어서 출력
- 메모리 큼
- 속도 빠름
- 문자열만 출력 가능
"""
import sys
print = sys.stdout.write

sys.stdout.write('a' + '＼n')
sys.stdout.write('b' + '＼n')


answer = 7
print(f"정답은 {answer}입니다.")
