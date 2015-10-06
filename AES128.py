'''  ======================================================================== 

                                    주 의 사 항


    1. 구현은 다양한 방식으로 이뤄질 수 있음
    2. AES128(...) 함수의 호출과 리턴이 여러번 반복되더라도 메모리 누수가 생기지 않게 함
    3. AddRoundKey 함수를 구현할 때에도 파라미터 rKey는 사전에 선언된 지역 배열을 가리키도록 해야 함
       (정확한 구현을 위해서는 포인터 개념의 이해가 필요함)
    4. 배열의 인덱스 계산시 아래에 정의된 KEY_SIZE, ROUNDKEY_SIZE, BLOCK_SIZE를 이용해야 함
       (상수 그대로 사용하면 안됨. 예로, 4, 16는 안되고 KEY_SIZE/4, BLOCK_SIZE로 사용해야 함)

 * ======================================================================== '''

#include "AES128.h" 
'// 암호화 모드'
ENC = 1 
'// 복호화 모드'
DEC = 0 

KEY_SIZE = 16
ROUNDKEY_SIZE = 176
BLOCK_SIZE = 16

'''기타 필요한 전역 변수 추가 선언'''



'''/*  <키스케줄링 함수>
 *   
 *  key         키스케줄링을 수행할 16바이트 키
 *  roundKey    키스케줄링의 결과인 176바이트 라운드키가 담길 공간
 */
'''
def expandKey(*key, *roundKey) :

    /* 추가 구현 */



'''/*  <SubBytes 함수>
 *   
 *  block   SubBytes 수행할 16바이트 블록. 수행 결과는 해당 배열에 바로 반영
 *  mode    SubBytes 수행 모드
 */'''
def subBytes(*block, mode) :

    /* 필요하다 생각하면 추가 선언 */

    switch(mode){

        case ENC:
            
            /* 추가 구현 */
            
            break;

        case DEC:

            /* 추가 구현 */
            
            break;

        default:
            fprintf(stderr, "Invalid mode!\n");
            exit(1);
    }
    
    return block;
}


'''/*  <ShiftRows 함수>
 *   
 *  block   ShiftRows 수행할 16바이트 블록. 수행 결과는 해당 배열에 바로 반영
 *  mode    ShiftRows 수행 모드
 */'''
def shiftRows(*block, mode) :

    '/* 필요하다 생각하면 추가 선언 */   '

    if mode==1 :
'            /* 추가 구현 */'
            
            break;

    else if mode == 0 :

            '/* 추가 구현 */'
            
            break;

        default:
            fprintf(stderr, "Invalid mode!\n");
            exit(1);
    }
    
    return block;
}


'''/*  <MixColumns 함수>
 *   
 *  block   MixColumns을 수행할 16바이트 블록. 수행 결과는 해당 배열에 바로 반영
 *  mode    MixColumns의 수행 모드
 */'''
def mixColumns(*block, mode) :

    '/* 필요하다 생각하면 추가 선언 */'   

    switch(mode){

        case ENC:
            
            '/* 추가 구현 */'
            
            break;

        case DEC:

            '/* 추가 구현 */'
            
            break;

        default:
            fprintf(stderr, "Invalid mode!\n");
            exit(1);
    }
    
    return block;
}


'''/*  <AddRoundKey 함수>
 *   
 *  block   AddRoundKey를 수행할 16바이트 블록. 수행 결과는 해당 배열에 반영
 *  rKey    AddRoundKey를 수행할 16바이트 라운드키
 */'''
def addRoundKey(*block, *rKey):

    '/* 추가 구현 */'

    return block;
}


'''/*  <128비트 AES 암호화 함수>
 *   
 *  plain   바이트 배열로 구성된 평문 (16바이트 고정)
 *  key     128비트 암호키 (16바이트)
 *
 *  @ret    암호화된 암호문
 */'''
def encrypt(*plain, *key) :
    roundKey[ROUNDKEY_SIZE];

    '/* 추가 구현 */'

}


'''/*  <128비트 AES 복호화 함수>
 *   
 *  cipher  바이트 배열로 구성된 평문 (16바이트 고정)
 *  key     128비트 암호키 (16바이트)
 *
 *  @ret    복호화된 평문
 */'''
def decrypt(*cipher, *key) :
    roundKey[ROUNDKEY_SIZE];
    
'    /* 추가 구현 */'

}


'''/*  <128비트 AES 암복호화 함수>
 *  
 *  mode가 ENC일 경우 평문을 암호화하고, DEC일 경우 암호문을 복호화하는 함수
 *
 *  [ENC 모드]
 *  plain   평문 바이트 배열
 *  cipher  결과(암호문)이 담길 바이트 배열. 호출하는 사용자가 사전에 메모리를 할당하여 파라미터로 넘김
 *  key     128비트 암호키 (16바이트)
 *
 *  [DEC 모드]
 *  plain   결과(평문)가 담길 바이트 배열. 호출하는 사용자가 사전에 메모리를 할당하여 파라미터로 넘김
 *  cipher  암호문 바이트 배열
 *  key     128비트 암호키 (16바이트)
 */'''
def AES128(*plain, *cipher, *key, mode) :
    tmp[]

    if(mode == ENC) :
        tmp = encrypt(plain, key);

        /* 추가 작업이 필요하다 생각하면 추가 구현 */    

    }else if(mode == DEC){
        tmp = decrypt(cipher, key);

        /* 추가 작업이 필요하다 생각하면 추가 구현 */    

    }else{
        fprintf(stderr, "Invalid mode!\n");
        exit(1);
    }
}
