def count_substring(s, ss):
    count = 0
    for i in range(0, len(s) - len(ss) + 1):
        chunk = s[i:i+len(ss)] 
        # e.g. if "foobar" and "foo", then chunk would be "foo"
        # on the next iteration, chunk will be "oob", etc...
        print(f"when i is {i}, chunk is {chunk}")
        if chunk == ss:
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    ss = input().strip()
    result = count_substring(s, ss)

