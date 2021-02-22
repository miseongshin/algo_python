all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

#1 반복 : O(n^2)


def get_absent_student(all_array, present_array):
    student_dict={}
    for key in all_students:
        student_dict[key]=True
    for key in present_array:
        del student_dict[key]

    for key in student_dict.keys():
        return key


#O(N), 공간복잡도 O(N)
print(get_absent_student(all_students, present_students))