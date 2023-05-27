

acces: 
	chmod +x stockholm.py

run:
	python3 stockholm.py

crypt:
	python3 stockholm.py

crypt_silent:
	python3 stockholm.py --silent

decrypt:
	python3 stockholm.py --reverse $(key)

decrypt_silent:
	python3 stockholm.py --reverse $(key) --silent

help:
	python3 stockholm.py -h


setup:
	mkdir -p $(HOME)/infection
	echo "Test data" > $(HOME)/infection/test1.der
	echo "Test data" > $(HOME)/infection/test2.pfx
	echo "Test data" > $(HOME)/infection/test3.key
	echo "Test data" > $(HOME)/infection/test4.crt
	echo "Test data" > $(HOME)/infection/test5.csr
	echo "Test data" > $(HOME)/infection/test6.p12
	echo "Test data" > $(HOME)/infection/test7.pem
	echo "Test data" > $(HOME)/infection/test8.odt
	echo "Test data" > $(HOME)/infection/test9.ott
	echo "Test data" > $(HOME)/infection/test10.sxw
	echo "Test data" > $(HOME)/infection/test11.stw
	echo "Test data" > $(HOME)/infection/test12.uot
	echo "Test data" > $(HOME)/infection/test13.3ds
	echo "Test data" > $(HOME)/infection/test14.max
	echo "Test data" > $(HOME)/infection/test15.3dm