  /*Early version just declared variable 
  START  
  let ansValues = [ m_value = 0,   c_value = 0, x_value = 0,  v_value = 0,  i_value = 0]
  const letterValues = [ 1000, 100, 10, 5, 1]

   ansValues = letterValues.map(ansValues =>  while(num>ansvalue Math.floor(num/letterValues)  )  

   
   return `${m_value}, ${c_value}, ${x_value}, ${v_value}, ${i_value} `;
   END
   */


/*letter value mapping 
  M = 1000
  D = 500
  C = 100
  L = 50 
  X = 10 
  V = 5
  I = 1
*/ 



function toRomanLazy(num) {
//inialize values so I know they hold a javascript number
let m_value = 0  
let c_value = 0 
let x_value = 0  
let v_value = 0  
let i_value = 0
//inialize emptystring, so I can push on letters
let ansString = ""

//divde by the valuse of the letter m=1000, c=100 x=10 v=5 i=1 and floor to drop decimal. 
//Next, subract off the value just calculated from num
//Finally use for loop and conditionalstatements to construct the string. 
//----Start m
m_value = Math.floor(num/1000)

if( m_value>=4 ){
  return "Sorry Romans could not think that big. The number must be less then 3,999"
}  

else if(m_value>0){
   num = num-m_value*1000
   for(i=0; i<m_value; i++){
    ansString = ansString+"M"
   }
}
     
  
//----Start C 
 c_value = Math.floor(num/100)
 if(c_value>0){
    num = num-c_value*100
    

      if(c_value>=5){
        ansString = ansString + "D"
        for(i=0; i<c_value%5; i++){
        ansString = ansString+"C"
        }
        
        
      }
      else{
      for(i=0; i<c_value; i++){
      ansString = ansString+"C"   
      }
      }
 }
 //---Start CXV */ 
 x_value = Math.floor(num/10)
 if(x_value>0){
    num = num-x_value*10
    

      if(x_value>=5){
        for(i=0; i<x_value%5; i++){
          ansString = ansString+"X"
          }
          ansString = ansString + "L"
        
      }
      else{
      for(i=0; i<x_value; i++){
      ansString = ansString+"X"   
      }
      }
    }    
//--Start I
 i_value = num 
 
 if(i_value>=5){
  for(i=0; i<i_value%5; i++){
    ansString = ansString+"I"
   }
  ansString = ansString + "V"
    
 }
else{
  for(i=0; i<i_value; i++){
ansString = ansString+"I"   
  }
}


return ansString;
}

function toRoman(num){
  //inialize values so I know they hold a javascript number
    let m_value = 0  
    let c_value = 0 
    let x_value = 0  
    let v_value = 0  
    let i_value = 0
    //inialize emptystring, so I can push on letters
    let ansString = ""
  
    //divde by the valuse of the letter m=1000, c=100 x=10 v=5 i=1 and floor to drop decimal. 
    //Next, subract off the value just calculated from num
    //Finally use for loop and conditionalstatements to construct the string. 
  //----Start m
    m_value = Math.floor(num/1000)
  
  
    if(m_value>0){
       num = num-m_value*1000
       for(i=0; i<m_value; i++){
        ansString = ansString+"M"
       }
    }
         
      
  //----Start C 
     c_value = Math.floor(num/100)
     if(c_value>0){
        num = num-c_value*100
        
  
          if(c_value===9){
            ansString = ansString + "CM"
          }
           else if(c_value<=8 && c_value>5){ 
            ansString = ansString+"D"
            for(i=0; i<c_value%5; i++){
            ansString = ansString+"C"
            }
           }
            else if(c_value===5){
              ansString = ansString+"D"
            }
            else if(c_value===4){
              ansString = ansString +"CD"
            }
          
          else{
          for(i=0; i<c_value; i++){
          ansString = ansString+"C"   
          }
          }
        }
     //---Start x */ 
     x_value = Math.floor(num/10)
     if(x_value>0){
        num = num-x_value*10
        
  
          if(x_value===9){
            ansString = ansString + "XC"
          }
           else if(c_value<=8 && c_value>5){ 
            ansString = ansString+"L"
            for(i=0; i<c_value%5; i++){
            ansString = ansString+"X"
            }
           }
            else if(x_value===5){
              ansString = ansString+"L"
            }

            else if(x_value===4){
              ansString = ansString +"XL"
            }
          
          else{
          for(i=0; i<x_value; i++){
          ansString = ansString+"X"   
          }
        }
      }
      //--Start i
          i_value = Math.floor(num)
          if(i_value>0){
             
             
       
               if(i_value===9){
                 ansString = ansString + "IX"
               }
                else if(i_value<=8 && i_value>5){ 
                 ansString = ansString+"V"
                 for(i=0; i<c_value%5; i++){
                 ansString = ansString+"I"
                 }
                }
      
                 else if(i_value===5){
                   ansString = ansString+"V"
                 }

            else if(i_value===4){
              ansString = ansString +"IV"
            }
               
               else{
               for(i=0; i<i_value; i++){
               ansString = ansString+"I"   
               }
               }
            }
   if( m_value>=4 ){
      "Sorry Romans could not think that big. The number must be less then 3,999"
    }
  
    //return `${m_value}, ${c_value}, ${x_value}, ${i_value}  ${ansString}`;
    return ansString;
  }
  



module.exports = { toRoman, toRomanLazy };


 console.log(toRomanLazy(4))
 console.log(toRomanLazy(150))
 console.log(toRomanLazy(3999))
 console.log(toRomanLazy(944))
 console.log(toRoman(4))
 console.log(toRoman(150))
 console.log(toRoman(3999))
 console.log(toRoman(944))


