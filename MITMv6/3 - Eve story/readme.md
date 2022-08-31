# MITMv6 - Instruction Manual

### ⚙️ Enviroment Setup ⚙️
The attack will be over three virtual machines (NAT network):

  &emsp; ☺️ The first machine is Alice's machine.
 
  &emsp; ☺️ The second machine is Bob's machine.
 
  &emsp; 😈 The third machine is Eve's machine (the attacker machine).

### Related Downloads

  &emsp; 📥 In Alice's VM the following file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py) has to be downloaded.

  &emsp; 📥 In Bob's VM the following file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Bob_side.py) has to be downloaded.

  &emsp; 📥 In Eve's (attacker) VM all the files in the following directory [here](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve) have to be downloaded.

### Files Changes
  
  &emsp; 📝 In Alice's VM modify `alice_side.py` file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py) to your own interface and Bob's ip (lines 6 and 10 accordignly) as corresponding to your

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;setup.

  &emsp; 📝 In Eve's directory [here](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve) modify the whole     `network_details.py` file as corresponding to your Network's configurations. 

### How To Run

  &emsp; 🏃 In Eve's (attacker) VM run the `main.py` file from (inside) Eve's directory [MITMv6_by_Eve](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve).
  
  &emsp;&emsp;&nbsp;&nbsp; Note that the attack has successfully succeeded and `alice_side.py`, `bob_sice.py` are files for representation only, not beyond.

  &emsp; 🏃 In Bob's VM run the `Bob_side.py` file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Bob_side.py).

  &emsp; 🏃 In Alice's VM run the `alice_side.py` file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py).

  Now the secret conversation (of Alice and Bob) has fully revealed to the attacker Eve 😈.
