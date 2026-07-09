# Phần 1 - Phân tích logic

## 1. Vì sao dự án có Line Coverage cao nhưng vẫn còn nhiều bug logic?

Line Coverage chỉ đo lường số dòng code đã được thực thi khi chạy test. Điều này không đảm bảo rằng toàn bộ logic nghiệp
vụ đã được kiểm tra đầy đủ.

Một dự án có thể đạt 90% Line Coverage vì:

- Hầu hết các dòng code đã được chạy qua.
- Test chỉ tập trung vào các trường hợp thành công (happy case).
- Nhiều nhánh điều kiện như `if/else`, `switch`, `try/catch` chưa được kiểm thử đầy đủ.
- Các trường hợp lỗi, dữ liệu đặc biệt hoặc edge case chưa được xử lý.

Do đó:

- Logic sai ở các nhánh chưa được test vẫn tồn tại.
- Bug vẫn có thể xuất hiện trên staging hoặc production.
- Coverage cao tạo cảm giác “an toàn giả” về chất lượng hệ thống.

---

## 2. Phân biệt Line Coverage và Branch Coverage

| Tiêu chí                     | Line Coverage                            | Branch Coverage                      |
|------------------------------|------------------------------------------|--------------------------------------|
| Mục đích                     | Đo số dòng code đã chạy                  | Đo số nhánh logic đã chạy            |
| Tập trung                    | Dòng lệnh                                | Điều kiện và hướng xử lý             |
| Ví dụ                        | Chạy qua dòng `if` là được tính coverage | Phải chạy cả nhánh `true` và `false` |
| Khả năng phát hiện bug logic | Thấp hơn                                 | Cao hơn                              |
| Độ tin cậy                   | Có thể gây hiểu nhầm                     | Phản ánh chất lượng test tốt hơn     |

Line Coverage chỉ trả lời:
> “Code đã được chạy chưa?”

Trong khi Branch Coverage trả lời:
> “Tất cả hướng xử lý logic đã được kiểm tra chưa?”

---

## 3. Vì sao Branch Coverage quan trọng hơn?

Branch Coverage quan trọng hơn vì:

- Đảm bảo mọi nhánh logic đều được kiểm thử.
- Giúp phát hiện lỗi ở các điều kiện đặc biệt.
- Kiểm tra được cả trường hợp thành công và thất bại.
- Giảm nguy cơ bug lọt lên staging/production.

Trong thực tế:

- Nhiều bug xuất hiện ở nhánh `else`, `default`, `catch`.
- Nếu chỉ nhìn Line Coverage thì các lỗi này rất dễ bị bỏ sót.

Vì vậy:

- Line Coverage chỉ phản ánh mức độ thực thi code.
- Branch Coverage phản ánh mức độ kiểm thử logic thực tế.

---

## 4. Ví dụ minh họa

### Ví dụ 1 - Điều kiện if/else

```java
public class AgeService {

    public String checkAge(int age) {
        if (age >= 18) {
            return "Adult";
        } else {
            return "Underage";
        }
    }
}
```

### Test hiện tại

```text
checkAge(20);
```

### Phân tích

- Test đã chạy qua hàm nên Line Coverage có thể rất cao.
- Tuy nhiên nhánh `else` chưa từng được kiểm tra.
- Nếu nhánh `else` viết sai logic thì bug vẫn không bị phát hiện.

Ví dụ lỗi:

```text
return"Adult";
```

ở nhánh `else`.

### Vai trò của Branch Coverage

Branch Coverage sẽ phát hiện:

- Nhánh `true` đã chạy.
- Nhánh `false` chưa chạy.

=> QA cần bổ sung test:

```text
checkAge(15);
```

để kiểm tra đầy đủ logic.

---

### Ví dụ 2 - Xử lý ngoại lệ try/catch

```java
public class CalculatorService {

    public int divide(int a, int b) {
        try {
            return a / b;
        } catch (ArithmeticException e) {
            return 0;
        }
    }
}
```

### Test hiện tại

```text
divide(10,2);
```

### Phân tích

- Hàm đã được thực thi nên Line Coverage cao.
- Nhưng khối `catch` chưa từng chạy.
- Nếu xử lý lỗi trong `catch` sai thì bug vẫn tồn tại.

Ví dụ lỗi:

```text
return -1;
```

thay vì trả về `0`.

### Vai trò của Branch Coverage

Branch Coverage sẽ nhận ra:

- Luồng `try` đã chạy.
- Luồng `catch` chưa chạy.

=> Cần bổ sung test:

```text
divide(10,0);
```

để kiểm tra logic xử lý ngoại lệ.

---

## 5. Kết luận

- Line Coverage cao không đồng nghĩa với việc phần mềm ít bug.
- Nó chỉ cho biết code đã được chạy trong quá trình test.
- Branch Coverage giúp kiểm tra đầy đủ các hướng xử lý logic.
- Theo dõi Branch Coverage sẽ giúp phát hiện lỗi nghiệp vụ tiềm ẩn tốt hơn và nâng cao chất lượng hệ thống.