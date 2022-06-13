import streamlit as st
import string

st.title("Lexical Analyzer and Parse")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Verb: Kedek, Sedek, Ningeh, Ningal, Ningting")

with col2:
    st.subheader("Noun: Aji, Beli, Hima, Motor, Jero")



text_input = st.text_input("Masukkan kalimat (dalam bahasa Bali): ")

st.markdown(f"Kalimat yang di input: {text_input}")

sentence = text_input
SInput = sentence.lower() + '#'


alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1','q2','q3','q4','q5','q6', 'q7','q8', 'q9','q10','q11','q12','q13', 'q14', 'q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31']

transisi_tabel = {}

for state in state_list:
  for alphabet in alphabet_list:
      transisi_tabel[(state, alphabet)] = 'error'
  transisi_tabel[(state, '#')] = 'error'
  transisi_tabel[(state, ' ')] = 'error'

#menambahkan ' ' sebelum input string
transisi_tabel['q0', ' '] = 'q0'

transisi_tabel[('q0', 'n')] = 'q1'
transisi_tabel[('q1', 'i')] = 'q2'
transisi_tabel[('q2', 'n')] = 'q3'
transisi_tabel[('q3', 'g')] = 'q4'
transisi_tabel[('q4', 't')] = 'q5'
transisi_tabel[('q5', 'i')] = 'q6'
transisi_tabel[('q6', 'n')] = 'q7'
transisi_tabel[('q7', 'g')] = 'q8'

transisi_tabel[('q4', 'e')] = 'q10'
transisi_tabel[('q10', 'h')] = 'q8'

transisi_tabel[('q4', 'a')] = 'q9'
transisi_tabel[('q9', 'l')] = 'q8'

transisi_tabel[('q0', 'k')] = 'q11'
transisi_tabel[('q11', 'e')] = 'q12'
transisi_tabel[('q12', 'd')] = 'q13'
transisi_tabel[('q13', 'e')] = 'q14'
transisi_tabel[('q14', 'k')] = 'q8'

transisi_tabel[('q0', 's')] = 'q15'
transisi_tabel[('q15', 'e')] = 'q12'



transisi_tabel[('q0', 'a')] = 'q16'
transisi_tabel[('q16', 'j')] = 'q17'
transisi_tabel[('q17', 'i')] = 'q8'

transisi_tabel[('q0', 'b')] = 'q18'
transisi_tabel[('q18', 'e')] = 'q19'
transisi_tabel[('q19', 'l')] = 'q20'
transisi_tabel[('q20', 'i')] = 'q8'

transisi_tabel[('q0', 'h')] = 'q21'
transisi_tabel[('q21', 'i')] = 'q22'
transisi_tabel[('q22', 'm')] = 'q23'
transisi_tabel[('q23', 'a')] = 'q8'

transisi_tabel[('q0', 'm')] = 'q24'
transisi_tabel[('q24', 'o')] = 'q25'
transisi_tabel[('q25', 't')] = 'q26'
transisi_tabel[('q26', 'o')] = 'q27'
transisi_tabel[('q27', 'r')] = 'q8'

transisi_tabel[('q0', 'j')] = 'q28'
transisi_tabel[('q28', 'e')] = 'q29'
transisi_tabel[('q29', 'r')] = 'q30'
transisi_tabel[('q30', 'o')] = 'q8'

transisi_tabel[('q31', 'n')] = 'q1'
transisi_tabel[('q31', 'k')] = 'q11'
transisi_tabel[('q31', 's')] = 'q15'
transisi_tabel[('q31', 'a')] = 'q16'
transisi_tabel[('q31', 'b')] = 'q18'
transisi_tabel[('q31', 'h')] = 'q21'
transisi_tabel[('q31', 'm')] = 'q24'
transisi_tabel[('q31', 'j')] = 'q28'


transisi_tabel[('q8', ' ')] = 'q31'
transisi_tabel[('q8', '#')] = 'accept'
transisi_tabel[('q31', '#')] = 'accept'
transisi_tabel[('q31', ' ')] = 'q31'

idx_char = 0
state = 'q0'
current_token = ''

while state != 'accept':
  current_char = SInput[idx_char]
  current_token += current_char
  state = transisi_tabel[(state, current_char)]
  if state == 'q8':
    st.write('Token: ', current_token, ', valid')
    current_token = ''
  if text_input == '':
    break

  if state == 'error':
    st.error('Tidak sesuai dengan yang tersedia, tidak bisa dilanjutkan.')
    break
  idx_char = idx_char + 1

#Conclusion 
if state == 'accept':
  lexical_valid = True
else :
  lexical_valid = False


tokens = sentence.lower().split()
tokens.append('EOS')


nTerminal = ['S', 'NN', 'VB']
Terminal = ['kedek', 'sedek', 'ningeh', 'ningal', 'ningting', 'aji', 'beli', 'hima', 'motor', 'jero']


#parse definisi tabel
parseT = {}

parseT[('S', 'aji')] = ['NN', 'VB', 'NN']
parseT[('S', 'beli')] = ['NN', 'VB', 'NN']
parseT[('S', 'jero')] = ['NN', 'VB', 'NN']
parseT[('S', 'motor')] = ['NN', 'VB', 'NN']
parseT[('S', 'hima')] = ['NN', 'VB', 'NN']
parseT[('S', 'kedek')] = ['error']
parseT[('S', 'sedek')] = ['error']
parseT[('S', 'ningeh')] = ['error']
parseT[('S', 'ningal')] = ['error']
parseT[('S', 'ningting')] = ['error']


parseT[('NN', 'aji')] = ['aji']
parseT[('NN', 'beli')] = ['beli']
parseT[('NN', 'jero')] = ['jero']
parseT[('NN', 'motor')] = ['motor']
parseT[('NN', 'hima')] = ['hima']
parseT[('NN', 'kedek')] = ['error']
parseT[('NN', 'sedek')] = ['error']
parseT[('NN', 'ningeh')] = ['error']
parseT[('NN', 'ningal')] = ['error']
parseT[('NN', 'ningting')] = ['error']


parseT[('VB', 'aji')] = ['error']
parseT[('VB', 'beli')] = ['error']
parseT[('VB', 'jero')] = ['error']
parseT[('VB', 'motor')] = ['error']
parseT[('VB', 'hima')] = ['error']
parseT[('VB', 'kedek')] = ['kedek']
parseT[('VB', 'sedek')] = ['sedek']
parseT[('VB', 'ningeh')] = ['ningeh']
parseT[('VB', 'ningal')] = ['ningal']
parseT[('VB', 'ningting')] = ['ningting']


stack = []
stack.append('#')
stack.append('S')
if text_input == '':
  print()
elif lexical_valid:
  st.success('Semua token di input: "%s" Valid!\n' %(sentence))
else :
  st.write('Sentence "%s" tidak diproses karena pada lexical analyzer tidak valid.\n' %(sentence))

#input inisiasi
idx_token = 0
symbol = tokens[idx_token]

#proses parsing
if lexical_valid:
  while(len(stack) > 0):
    top = stack[len(stack)-1]
    
    if top in Terminal:
      if top == symbol:
        stack.pop()
        idx_token = idx_token + 1
        symbol = tokens[idx_token]
        if symbol == 'EOS':
          stack.pop()
      else:
        st.write('error')
        break
    elif top in nTerminal:
      if parseT[(top, symbol)][0] != 'error':
        stack.pop()
        pushSymbol = parseT[(top, symbol)]
        for i in range(len(pushSymbol)-1,-1,-1):
          stack.append(pushSymbol[i])
      else:
        st.write('error')
        break

    else:
      st.write('error')
      break
    st.write("\n\n")

  if symbol == 'EOS' and len(stack) == 0:
    st.write('Input string "%s" diterima dan sesuai grammar!' %(sentence))
  else:
    st.error('Error, string "%s" tidak diterima karena tidak sesuai grammar!' %(sentence))

