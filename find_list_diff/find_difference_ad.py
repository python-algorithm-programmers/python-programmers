def extract_fd_subfolders(filepath):
    """주어진 파일에서 'FD/' 바로 뒤의 폴더명만 추출하여 집합으로 반환"""
    subfolders = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # 'FD/'가 포함된 줄에서만 처리
            if "AD/" in line:
                # 줄바꿈 문자 제거 및 '/'를 기준으로 경로 분리
                parts = line.strip().split('/')
                if parts[1] != "":
                    subfolders.add(parts[1])
    return subfolders

def extract_subfolders(filepath):
    """주어진 파일에서 'FD/' 바로 뒤의 폴더명만 추출하여 집합으로 반환"""
    subfolders = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # 줄바꿈 문자 제거 및 집합에 추가
            clean_line = line.strip()
            if clean_line != '':
                subfolders.add(clean_line)
    return subfolders

def find_difference_and_write(ad_rev_list_path, ad_total_list_path, output_path):
    ad_rev_subfolders = extract_subfolders(ad_rev_list_path)
    ad_total_subfolders = extract_fd_subfolders(ad_total_list_path)
    difference = ad_total_subfolders - ad_rev_subfolders

    print("ad_rev_subfolders (First 5):", sorted(list(ad_rev_subfolders))[:5])
    print("ad_total_subfolders (First 5):", sorted(list(ad_total_subfolders))[:5])
    print("len_ad_rev_subfolders", len(ad_rev_subfolders))
    print("len_ad_total_subfolders", len(ad_total_subfolders))


    with open(output_path, 'w', encoding='utf-8') as file:
        if difference:
            for folder in sorted(difference):
                file.write(f"{folder}\n")
        else:
            file.write("No difference found between the lists.\n")

if __name__ == '__main__':
    ad_rev_list_path = 'C:/Users/abc/diff_ad.txt'
    ad_total_list_path = 'C:/Users/abc/ad_final.txt'
    output_path = 'C:/Users/abc/diff_ad_final.txt'
    find_difference_and_write(ad_rev_list_path, ad_total_list_path, output_path)
