input = "73167176531330624919225119674426574742355349194934"
input += "96983520312774506326239578318016984801869478851843"
input += "85861560789112949495459501737958331952853208805511"
input += "12540698747158523863050715693290963295227443043557"
input += "66896648950445244523161731856403098711121722383113"
input += "62229893423380308135336276614282806444486645238749"
input += "30358907296290491560440772390713810515859307960866"
input += "70172427121883998797908792274921901699720888093776"
input += "65727333001053367881220235421809751254540594752243"
input += "52584907711670556013604839586446706324415722155397"
input += "53697817977846174064955149290862569321978468622482"
input += "83972241375657056057490261407972968652414535100474"
input += "82166370484403199890008895243450658541227588666881"
input += "16427171479924442928230863465674813919123162824586"
input += "17866458359124566529476545682848912883142607690042"
input += "24219022671055626321111109370544217506941658960408"
input += "07198403850962455444362981230987879927244284909188"
input += "84580156166097919133875499200524063689912560717606"
input += "05886116467109405077541002256983155200055935729725"
input += "71636269561882670428252483600823257530420752963450"


maxProduct = 0
for i in range(4, len(input)):
	tempProduct = 1
	for j in range(i-4, i+1):
		tempProduct *= int(input[j])
	maxProduct = max(maxProduct, tempProduct)
print(maxProduct)