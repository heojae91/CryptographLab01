'''/*  ======================================================================== *

                                    주 의 사 항


    1. 계산 중간 흐름은 다음 문서를 보고 비교하는 것을 추천함

		http://grouper.ieee.org/groups/1619/email/pdf00037.pdf

 *  ======================================================================== */'''

#include <stdio.h>
#include "XTS_AES.h"

iv[]  = { 
	'// 직접 작성해서 테스트'
};

key[] = { 
	'// 직접 작성해서 테스트'
};

plain[] = { 
	'// 직접 작성해서 테스트'
};

cipher[] = { 
	'// 직접 작성해서 테스트'
};

tmp[64];

'// 암호화 테스트'
XTS_AES128(plain, tmp, 64, ENC);
print ("XTS_AES Encryption: %s\n", 0 == strncmp((char*) cipher, (char*) tmp, 64) ? "SUCCESS!" : "FAILURE!");

'// 복호화 테스트'
XTS_AES128(tmp, cipher, 64, DEC);
print ("XTS_AES Decryption: %s\n", 0 == strncmp((char*) tmp, (char*) plain, 64) ? "SUCCESS!" : "FAILURE!");