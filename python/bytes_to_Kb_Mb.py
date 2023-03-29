t = int(input())
m = []
for i in range(t):
    m.append(int(input()))

  
for item in m:
    m_kb = item // 1024
    if m_kb < 1 :
        print(f"{item}B")
    else:
        m_mb = m_kb // 1024
        if m_mb < 1:
            print(f"{m_kb}KiB")
        else:
            print(f"{m_mb}MiB")
