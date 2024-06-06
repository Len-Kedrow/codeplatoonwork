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

const toRomanLazy = (num) =>{
//inialize values so I know they hold a javascript number
  let m_value = 0  
  let c_value = 0 
  let x_value = 0  
  let v_value = 0  
  let i_value = 0
  //inialize emptystring, so I can push on letters
  let ansString = " "

  //divde by the valuse of the letter m=1000, c=100 x=10 v=5 i=1 and floor to drop decimal. 
  //Next, subract off the value just calculated from num
  //Finally use for loop and conditionalstatements to construct the string. 

   m_value = Math.floor(num/1000)
   num = num-m_value*1000

  for(i=0; i<m_value; i++){
    ansString = ansString+"M"
  }   

   c_value = Math.floor(num/100)
   num = num-c_value*100

   if(c_value>5){
      ansString = ansString + "D"
      for(i=0; i<c_value%5-1; i++){
        ansString = ansString+"C"
      }
   }
   else{
      for(i=0; i<c_value; i++){
    ansString = ansString+"C"   
      }
    }
   x_value =Math.floor(num/10)
   num = num-x_value*10

   if(x_value>5){
    ansString = ansString + "L"
    for(i=0; i<(x_value%5-1); i++){
      ansString = ansString+"X"
      }
   }
 else{
    for(i=0; i<x_value; i++){
  ansString = ansString+"X"   
    }
  }

   i_value = num 

   if(i_value>5){
    ansString = ansString + "V"
      for(i=0; i<i_value%5-1; i++){
      ansString = ansString+"I"
     }
   }
 else{
    for(i=0; i_value<i; i++){
  ansString = ansString+"I"   
    }
  }
  
 if( m_value>=4 ){
    "Sorry Romans could not think that big. The number must be less then 3,999"
  }

  return `${m_value}, ${c_value}, ${x_value}, ${i_value}  ${ansString}`;
}

function toRoman(num) {
  return "";
}

module.exports = { toRoman, toRomanLazy };


console.log(toRomanLazy(3999))
