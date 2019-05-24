import struck

def offset_generator(student_id)
  start = 54

  for 1 in student_id:
      t = int(i)
      if t == 0:
          t = 10

      start += t * 3
      yield start

def tamper_st lenna: str(id)
  with open('lenna.bmp','r+b') as f:
      for i in offset_generator(student_id):
          print(i)
          f.seek(i)
          f.write(b'\x00\x00\x00')

if __name__='__main__'
import sys
tamper_st(sys.argv[1])
