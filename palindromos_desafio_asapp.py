n = int(raw_input())
s = raw_input()
ans = [[None]*n for _ in range(n)]

for i in range(n):
	ans[i][i] = 0
	if i+1 < n:
		ans[i][i+1] = 0 if s[i] == s[i+1] else 1

for l in range(2, n):
	for i in range(n-l):
		j = i+l
		if s[i] == s[j]:
			ans[i][j] = ans[i+1][j-1]
		else:
			ans[i][j] = 1 + min(ans[i+1][j], ans[i][j-1])

print(ans[0][n-1])
