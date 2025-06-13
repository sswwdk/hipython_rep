#간식박스 관리 프로그램
snack_box = ['초콜릿','하리보','껌']
new_snack = input("##먹고 싶은 간식을 추가하세요.").split(",") #단, 쉼표(,)로 연결하세요
snack_box += new_snack

print(snack_box)

#간식박스 관리 프로그램2
qty= int(input("##간식박스 몇 세트로 포장할까요?"))
snack_box *= qty
print(snack_box)


print(f"주문하신 간식상자는 {snack_box[0]},{snack_box[1]},{snack_box[2]},{snack_box[3]} 등입니다. 확인해주세요")

#간식박스 관리 프로그램3
msg = f"##혹시 빼고 싶은 간식이 있으면 번호를 입력하세요 (0~{len(snack_box)-1})"
snack_no = int(input(msg))
del snack_box[snack_no]

print(snack_box)

#간식박스 관리 프로그램 4
# 찾고 싶은 간식이름을 입력하세요
#있어요 OR 없어요 출력
snack_box
find = input("##찾고 싶은 간식 이름을 작성하세요")
find in snack_box

if find in snack_box:
    print("있어요")
else:
    print("없어요")

#간식박스 관리 프로그램 5
print("##주문하신 간식박스는 위에서부터 다음과 같습니다.")
print(f"{snack_box[::-1]}, 총 {len(snack_box)}개 입니다") # 뒤에서부터 출력 snack_box[::-1]