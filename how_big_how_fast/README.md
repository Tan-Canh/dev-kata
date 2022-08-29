# [Kata03: How Big? How Fast?](http://codekata.com/kata/kata03-how-big-how-fast/)

Rough estimation is a useful talent to possess. As you’re coding away, you may suddenly need to work out approximately how big a data structure will be, or how fast some loop will run. The faster you can do this, the less the coding flow will be disturbed.

So this is a simple kata: a series of questions, each asking for a rough answer. Try to work each out in your head. I’ll post my answers (and how I got them) in a week or so.

# How Big?

- roughly how many binary digits (bit) are required for the unsigned representation of:
  - 1,000
  - 1,000,000
  - 1,000,000,000
  - 1,000,000,000,000
  - 8,000,000,000,000

- My town has approximately 20,000 residences. How much space is required to store the names, addresses, and a phone number for all of these (if we store them as characters)?

- I’m storing 1,000,000 integers in a binary tree. Roughly how many nodes and levels can I expect the tree to have?
- Roughly how much space will it occupy on a 32-bit architecture?

---

[Binary digits (bit)](https://www.gartner.com/en/information-technology/glossary/bit-binary-digit#:~:text=A%20binary%20digit%20(bit)%20is,and%20processed%20by%20the%20computer.)
[Unsigned and signed integers](https://www.ibm.com/docs/en/aix/7.2?topic=types-signed-unsigned-integers)
[Converter](https://www.rapidtables.com/convert/number/decimal-to-binary.html)
[Doc](https://byjus.com/maths/decimal-to-binary/))

example convert decimal (base 10) to binary (base 2)

| Devide by 2 | Result | Remainder | Binary                   |
| ----------- | ------ | --------- | ------------------------ |
| 1000:2      | 500    | 0         | 0                        |
| 500:2       | 250    | 0         | 0                        |
| 250:2       | 125    | 0         | 0                        |
| 125:2       | 62     | 1         | 1                        |
| 62:2        | 31     | 0         | 0                        |
| 31:2        | 15     | 1         | 1                        |
| 15:2        | 7      | 1         | 1                        |
| 7:2         | 3      | 1         | 1                        |
| 3:2         | 1      | 1         | 1                        |
| 1:2         | 0      | 1         | 1                        |
|             |        |           | **len(1111101000) = 10** |

1,000  -> len("1111101000") = 10
1,000,000  -> len("11110100001001000000") = 20
1,000,000,000  -> len("111011100110101100101000000000") = 30
1,000,000,000,000  -> len("1110100011010100101001010001000000000000") = 40
8,000,000,000,000  -> len("1110100011010100101001010001000000000000000") = 43

[Binary tree](https://www.geeksforgeeks.org/binary-tree-data-structure/)
[Char to bit](https://www.ibm.com/docs/en/ibm-mq/7.5?topic=platforms-standard-data-types) and [why](https://stackoverflow.com/questions/4850241/how-many-bits-or-bytes-are-there-in-a-character) [a char == 8 bits (1 byte)](https://stackoverflow.com/questions/9727465/will-a-char-always-always-always-have-8-bits#:~:text=that%20a%20char%20is%20represented,of%20RAM%20(%2B%20swap%20space).)

---

# How Fast?

- My copy of Meyer’s Object Oriented Software Construction has about 1,200 body pages. Assuming no flow control or protocol overhead, about how long would it take to send it over an async 56k baud modem line?

- My binary search algorithm takes about 4.5mS to search a 10,000 entry array, and about 6mS to search 100,000 elements. How long would I expect it to take to search 10,000,000 elements (assuming I have sufficient memory to prevent paging).

- Unix passwords are stored using a one-way hash function: the original string is converted to the ‘encrypted’ password string, which cannot be converted back to the original string. One way to attack the password file is to generate all possible cleartext passwords, applying the password hash to each in turn and checking to see if the result matches the password you’re trying to crack. If the hashes match, then the string you used to generate the hash is the original password (or at least, it’s as good as the original password as far as logging in is concerned). In our particular system, passwords can be up to 16 characters long, and there are 96 possible characters at each position. If it takes 1mS to generate the password hash, is this a viable approach to attacking a password?

---
[Baud](https://en.wikipedia.org/wiki/Baud)
[Bit rate & baud rate](https://ttmn.mobi/toc-do-baud-la-gi/)
Giả sử các ký tự trong quyển sách đều là ký tự latinh => 1 char = 8 bits
Giả sử trung bình một dòng chứa 100 ký tự => 1 line = 100 chars = 800 bits
Giả sử trung bình một trang chứa 50 dòng => 1 page = 50 lines = 40.000 bits
Vậy quyển sách với 1.200 trang => 48.000.000 bits

Giả sử modem là kiểu cũ, khi mà 1 bdps = 1 bps => 48.000.000 / 56.000 ~= 857s (~14 phút)
Đối với các modem kiểu mới tùy thuộc vào kiến trúc, giả sử 1bdps = 5bps => 48.000.000 / (56.000 * 5) ~= 171s (~2.85 phút) nhanh hơn ~7 lần

---
Như đã làm ở phần 1, nếu lưu vào cây nhị phân
10.000 records, ta sẽ có cây nhị phân 15 cấp, tức là có 14 lần phân nhánh mất 4.5ms (đề cho) => 1 lần mất ~0.32ms
100.000 records => 18 cấp => 17 lần phân nhánh => 6ms (đề cho) => 1 lần mất ~0.35ms
10.000.000 => 25 cấp => 24 lần phân nhánh (lấy trung bình mỗi lần phân nhánh 0.34ms) => time = 8.16ms (~3.400s hay ~57 phút)

---
Tóm tắt, trong một hệ thống Unix cụ thể, mật khẩu sau khi hash có độ dài 16 ký tự, mỗi ký tự có 96 cách thay đổi, tức là có 16^96 chuỗi khả dụng
Nếu dùng phương pháp brute force để tấn công (với mỗi lần hash mất 1ms), trong trường hợp tệ nhất sẽ mất (16^96)ms = (2^384)/31,536,000,000 năm => bất khả thi
Trong quy mô nhỏ hơn, nếu chuỗi hash chỉ có 8 ký tự và giới hạn các ký tự đều là các chữ cái latinh in hoa, ta có 8^23 chuỗi khả dụng => mất 590,295,810,358,705,651,712ms hay ~18,718,157,355 năm để dò mật khẩu
