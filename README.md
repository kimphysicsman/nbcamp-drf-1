# nbcamp-drf-1
내일배움캠프 DRF 1일차 과제

## 스파르타코딩클럽
## 내일배움캠프 AI 웹개발자양성과정 2회차
## DRF 강의 1일차 과제

### 과제내용
 1. args, kwargs를 사용하는 예제 코드 짜보기
 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
 4. django에서 queryset과 object는 어떻게 다른지 서술하기
 
### 1. args, kwargs를 사용하는 예제 코드 짜보기
```python
def sum(num1, *args):
    if len(args) != 0:
        return num1 + sum(*args)
    else :
        print('--args example--')
        return num1

print(sum(1, 2, 3, 4, 5, 6, 7))

def print_info(**kwargs):
    print('--kwargs example--')
    if kwargs is not None:
        for item in kwargs.items():
            print(f'{item[0]} is {item[1]}')

print_info(name='dongwoo', year=29, weight=75, height=176)

```

###  2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기

#### 1) immutable
: int, float, bool, string, unicode, tuple 

#### 2) mutable
: list, dict, set (+ 사용자 정의 클래스)

#### 3) 특징
 - immutable 객체는 액세스가 더 빠르고 복사본을 생성해야 하기 때문에 변경 하는 데 비용이 많이 든다. 반대로 mutable 객체는 변경하기 쉽다.
 - 개체의 크기나 내용을 변경해야 하는 경우 가변 개체를 사용하는 것이 좋다.
 - 
 ```python
 tup = ([3, 4, 5], '내 이름')
 ```
위의 튜플은 리스트와 문자열로 구성된다. 문자열은 변경할 수 없으므로 값을 변경할 수 없지만 리스트의 내용은 변경될 수 있다. 따라서 튜플 자체는 변경할 수 없지만 변경 가능한 항목을 포함할 수 있다.

### 3. DB Field에서 사용되는 Key 종류와 특징 서술하기

#### 1) Foreign Key
: A many-to-one 관계를 나타내며 2가지의 인자(관계를 맺을 클래스와  on_delete option)가 필요하다.

- example
> ```python
>from django.db import models
>
>class AbstractCar(models.Model):
>    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
>
>    class Meta:
>        abstract = True
> ```

- on_delete option
 1) CASCADE : 삭제된 객체와 ForeignKey를 포함하는 객체도 삭제
 2) PROTECT : ForeignKey를 가진 객체를 삭제 방지
 3) RESTRICT : ForeignKey를 가진 객체를 삭제 방지 하지만 CASCADE에 의해 삭제될 수 있음
 4) SET_NULL : True인 경우에 null로 지정
 5) SET_DEFAULT : 기본 ForeignKey 설정
 6) SET() : 해당 값으로 설정
 7) DO_NOTHING : 아무 작업도 안함
 
#### 2) Primary Key
 : primary_key=True인 경우 모델의 기본 키가 된다.
null=False와 unique=True의 의미를 가지고 객체는 단하나의 primary key만 설정 가능
 

### 4. django에서 queryset과 object는 어떻게 다른지 서술하기

#### 1) object
: 정의한 모델로 생성한 실제 객체 데이터

#### 2) QuerySet
: DB에 저장된 object들의 집합
> Django Queryset - w3schools
>
> A QuerySet is a collection of data from a database.
>
> A QuerySet is built up as a list of objects.
>
> QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data.

### 5. 출처
- mutable vs immutable in python 
https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/

- Foriegn Key, Primary Key
https://docs.djangoproject.com/en/4.0/ref/models/fields/

- QuerySet
https://www.w3schools.com/django/django_queryset_get.php
