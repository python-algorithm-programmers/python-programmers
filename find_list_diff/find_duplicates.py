def extract_and_find_duplicates(filepath, keyword):
    """주어진 파일에서 특정 키워드가 있거나 없는 라인의 파일명을 추출하고 중복을 찾음"""
    with_train = set()
    without_train = set()
    duplicates_with_train = set()
    duplicates_without_train = set()

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if "AD" in line:
                parts = line.strip().split('/')
                if keyword in line:
                    # 'train'이 포함된 경우, parts[2]를 사용하여 중복 검사
                    if len(parts) > 2 and parts[2] in with_train:
                        duplicates_with_train.add(parts[2])
                    with_train.add(parts[2])
                else:
                    # 'train'이 포함되지 않은 경우, parts[1]를 사용하여 중복 검사
                    if len(parts) > 1 and parts[1] in without_train:
                        duplicates_without_train.add(parts[1])
                    without_train.add(parts[1])
    return duplicates_with_train, duplicates_without_train, without_train, with_train


def write_duplicates_to_file(duplicates_with_train, duplicates_without_train, output_path):
    """찾아낸 중복된 파일명을 파일에 기록"""
    with open(output_path, 'w', encoding='utf-8') as file:
        if duplicates_with_train:
            # file.write("Duplicates in 'with_train':\n")
            for item in duplicates_with_train:
                file.write(f"{item}\n")
        else:
            file.write("No duplicates found in 'with_train'.\n")

        file.write("\n")

        if duplicates_without_train:
            # file.write("Duplicates in 'without_train':\n")
            for item in duplicates_without_train:
                file.write(f"{item}\n")
        else:
            file.write("No duplicates found in 'without_train'.\n")


if __name__ == '__main__':
    filepath = 'C:/Users/abc/ad_rev.txt'
    output_path = 'C:/Users/abc/diff_ad.txt'
    duplicates_with_train, duplicates_without_train, without_train, with_train = extract_and_find_duplicates(filepath, "train")
    print("without_train", len(without_train))
    print("with_train", len(with_train))

    write_duplicates_to_file(duplicates_with_train, duplicates_without_train, output_path)

# unzip -l C:/Users/abc/Downloads/AD_rev.zip > ad_rev.txt