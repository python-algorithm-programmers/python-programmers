def solution(citations):
    sorted_citations = sorted(citations, key=lambda x:x, reverse=True)

    count = 0
    for citation in sorted_citations:
        if citation > count:
            count += 1
            continue

        else:
            break

    return count


if __name__ == '__main__':
    print(solution([3,2,2,2,0]))