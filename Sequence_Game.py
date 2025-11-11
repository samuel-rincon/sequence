import streamlit as st
import random
import re

def generate_sequence():
    fixed_sequence = [4, 8, 15, 16, 23, 42, 0, 0, 0, 0]  # No hagas trampa, Edward
    
    return {
        'method': "Mystery Pattern",
        'sequence': fixed_sequence,
        'formula_latex': r"a_n = \text{The Numbers}",
        'variables': {'A': 0, 'B': 0, 'X': 0, 'Y': 0}
    }

def main():
    st.set_page_config(page_title="Sequence Guessing Game", layout="centered")
    
    st.title("🧠 Sequence Guessing Game")
    st.markdown("Guess the next numbers in the sequence!")
    
    if 'game_data' not in st.session_state:
        st.session_state.game_data = generate_sequence()
        st.session_state.current_guess = 5  
        st.session_state.show_hint = False
        st.session_state.game_over = False
        st.session_state.gave_up = False
        st.session_state.correct_sequence_guessed = False
    
    seq = st.session_state.game_data['sequence']
    st.subheader("Sequence:")
    st.write(f"**{', '.join(map(str, seq[:4]))}**, ?, ?, ...")
    
    st.write(f"**Guess term #{st.session_state.current_guess}**")
    
    guess = st.number_input("Enter your guess:", step=1, format="%d")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Submit Guess") and not st.session_state.game_over:
            correct_answers = {5: 23, 6: 42} 
            
            if guess == correct_answers[st.session_state.current_guess]:
                st.success("✅ Correct!")
                st.session_state.current_guess += 1
                if st.session_state.current_guess > 6:
                    st.session_state.game_over = True
                    st.session_state.correct_sequence_guessed = True
                    st.balloons()
            else:
                st.error("❌ Incorrect! Try again.")
    
    with col2:
        if not st.session_state.show_hint and not st.session_state.game_over:
            if st.button("Show Next Term"):
                st.session_state.show_hint = True
                correct_answers = {5: 23, 6: 42}
                st.info(f"Term #{st.session_state.current_guess} is: **{correct_answers[st.session_state.current_guess]}**")
                st.session_state.current_guess += 1
                if st.session_state.current_guess > 6:
                    st.session_state.game_over = True
    
    with col3:
        if st.button("Give Up") and not st.session_state.game_over:
            st.session_state.game_over = True
            st.session_state.gave_up = True
            st.warning("You gave up! Here's the solution:")
    
    if st.session_state.game_over:
        st.markdown("---")

        if st.session_state.correct_sequence_guessed:
            st.subheader("🎉 CONGRATULATIONS! 🎉")
            st.markdown("""
No hay forma de volver. 

Mi única esperanza es que exista algo adelante para distraerme lo suficiente, pero no va a funcionar de noche jamás, porque el futuro es acumulativo. No se deja nada, todo permanece.
Todo lo llevas encima en cada paso.

Lo sé porque a pesar de todo, estoy dando los pasos. Los pasos correctos. Los pasos sanos. Ya estoy de pie porque por más que quisiera, es el peor momento de mi vida para quedarme sentado. Ya estoy andando, y el camino es hasta bonito. Soleado. Me puedo alejar todo lo que quiera, a toda velocidad, no importa.

Igual pesa. Así como todo lo que vale pesa.

Me prohibieron terminar el libro.

Uno de los pasos es hablar con alguien que sepa de lo que habla, y su opinión profesional es que en este punto, seguir leyendo solo es una forma de castigarme, que es lo que estoy tratando de evitar. Porque soy el tipo de persona que se pone de pie, porque tengo que hacerlo. Si me torturo en cada paso no voy a llegar a donde voy. Y tengo que llegar.

Entré en pánico. Nunca había sentido tanto miedo, y no sabía cómo manejarlo. Hice lo que hace todo animal acorralado: lo necesario para sobrevivir. Llorar, negociar, rezar. Lo necesario para que no le corten el aire.
Y el aire olía a ti.

Por eso no podía soportar tenerte cerca. Es la mayor tentación y la mayor tortura a la que me he sometido.

El olfato es el sentido con la mejor memoria. No puedo hacerlo olvidar así como no puedo hacerme olvidar, solo queda aceptarlo.

Quisiera que no valiera. Quisiera soltarlo y no recordarlo jamás, no sentirlo jamás. Quisiera jamás haber sentido la luz del sol porque ahora duele demasiado y no sé cómo lidiar con eso. El dolor, que es temporal, pero ¿Y la memoria, que es permanente? ¿El peso?
Está en todos lados y está en la nada. Especialmente en la nada. En el silencia y en la noche y en el frío, cuando estoy más seguro, con toda el alma, que no estoy donde pertenezco. 

Tu tienes claro dónde debería estar. Dónde pertenezco.

Más vale que no estés leyendo esto.

Si tomaste una decisión, no deberías estar aquí. No deberías seguir leyendo. Porque estás seguro de tu decisión.

Por supuesto que no entiendo tus razones. ¿Cómo voy a entenderlas, si no te conozco? Nos conocimos un mes, ni yo te conozco a ti ni tu me conoces a mí.

Aun así, fui completamente vulnerable contigo. Como nunca lo había sido con nadie, porque no pensé que hubiera alguien que pudiera entender el valor de eso, y tratarlo con cuidado.

Tu me trataste con cuidado hasta que ya no lo hiciste. En el espacio de una hora.

Respondí sin pensar porque así es como respondía contigo, sin dudarlo dos veces. Para mi eres algo seguro, porque la conexión es tan obvia. Las coincidencias son tantas que no podría ser otra cosa aparte del destino.

La persona que podría verme completamente al desnudo con lo que eso implica para mi. Ver eso, y sostenerme igual. Estaba completamente seguro.

No di un solo paso creyendo que podría terminar. Toda mi vida la he dedicado a las posibilidades, y me negué a ver las posibilidades. Eso fue una decisión mía. No es justo que te culpe por eso, porque no hay excusa.

Iba con los ojos cerrados.

Y tu alcanzaste a ver un pedazo de mi alma. Lo viste, hiciste el cálculo y no valía la pena el riesgo.

No valió la pena para terminar de conocerme.

Te retiraste temprano.

No fue suficiente para quedarte a ver quién soy ahora o quién seré mañana. Tu no sufres de curiosidad como yo.
¿Pero cómo se supone que no sea personal si no fui suficiente?

Puedes tener todas las convicciones del mundo. Yo he tenido tiempo de pensar, he tenido momentos de claridad en los que no duele demasiado para poder pensar, fríamente. En esos momentos he podido ver las cosas como son, no como se sienten.

Entiendo el problema.

Tu y yo tenemos los mismos principios, con prioridades muy distintas. Yo, en efecto, no soy una persona coherente.

Debes creer que tengo una voluntad muy débil, solo me conociste doblándola contigo. No me conociste defendiendo mis convicciones, no sabes qué estoy dispuesto a sacrificar para no ceder con mis creencias. Mucho, mucho, mucho, mucho.
No todo.

Porque contigo, fue natural ceder. En cosas pequeñas, sin importancia. En una hora más, un beso más, un mensaje más. Pensé que tu querías ceder, y correspondí. 

Esto es una cosa de una vez. Tu eres mi única excepción, y eso es todo lo que conoces. En toda mi vida, no haría una excepción por amor. Excepto en la única excepción. Ahí estamos en desacuerdo, y ahí radica el problema.

Tu serías la excepción a mis principios y yo no sería la excepción a los tuyos.

No tiene sentido renunciar a ellos por un hombre que conociste un mes. No tiene sentido alguno.

¿Podría haber sido una excepción algún día, si hubieras llegado a amarme?

Tal vez nunca hubieras llegado a amarme. Porque para ti esta no era la primera vez, tu ibas con cuidado, con los ojos abiertos.

Al final del día qué importa, si no estás dispuesto a tomar el riesgo. 

Ya no estoy acorralado y no tengo aire por el qué pelear.

Lo siento por mentir. Probablemente sentiste la misma traición que sentí yo.

Si tenía la intención de acostarme con él. No mentí cuando dije que pensé que podría haber algo después, y esa fue mi intención desde el principio, pero si fui es porque quería que me tocara. Quería que me sostuviera. Quería conocer la seguridad de unos brazos, la libertad de besar a mi gusto, de adorar por voluntad.

Y entonces estuve ahí, y no sentí absolutamente nada.

Así fue como llegué a esa convicción: no quiero esto.

Ya no quería que me tocara. Nunca lo quise, solo pensé que lo deseaba. Pero estaba equivocado, y ahí acabó.

Después conocí a Alejandro. Era caballero, afectivo, era serio. Y yo sabía que podía llegar a quererlo. Al final no funcionó, pero igual lo sufrí porque sabía que pude llegar a quererlo.

El problema es que a ti puedo llegar a amarte.

Lastimosamente, esa es mi terrible conclusión.

Que uno no puede amar a cualquiera, no se puede amar a múltiples. Solo al que es.

No fui vulnerable contigo por estúpido, o por falta de experiencia, o por ingenuo. Sino porque eres tú. Es obvio. Lo fue en ese momento, y lo odio con toma mi alma, pero lo es ahora.

Es mi convicción y no tienes que respetarla por mí.

Pero es demasiado obvio, Edward.

Crees que soy como crees que soy. Tienes toda la evidencia en contra, tienes un mes de mi alma en tus manos, tendrás el resto de mi vida. Pero la duda pesa más en tu decisión.
Tu no vas a tomar el riesgo, y tu y yo nos vamos a quedar así para siempre.

Tu eres el dueño de tus decisiones, de tus convicciones y tus prioridades. Eres el dueño de tu miedo y de tus apuestas.

Y yo no valgo el riesgo.

¿Qué más puedo hacer?

Seguir cometiendo errores como este, seguir condenándome a esperar. 

Sabes que no tengo opción. Ya va encima. Todo lo que tiene peso existe, y no puede dejar de existir. 

Solo me queda existir, esperando un valor que tal vez jamás llegue.

No me dejes si tienes dudas.

No me dejes si es tan obvio.

No me dejes.

No te engañes Edward, las personas no están para la coherencia, están para el amor. Están para hacer apuestas y perderlas. Están para hacer apuestas y ganarlas.

Es una creencia que va en contra de toda lógica. No tiene sentido alguno. Y yo, una persona de lógica, me encuentro creyéndola. 

¿Qué otra prueba necesito?

No lo digo como un capricho y no lo digo con pánico ni con miedo. Lo digo con lucidez. Lo digo con la fuerza que requiere tomar una decisión como esta, una decisión final y permanente. El peor error de mi vida y mi más grande apuesta: 

Llámame, e iré.

Hoy pagué el registro para el FM, 12 de Febrero de 2026. Espero que te vaya bien en el saber pro. Esperar a la cuarta hora es un fastidio. Por cierto, esa parte del libro si la leí.

No hay razones de peso para amarme, Samuel. No te engañes tu tampoco.

Yo debo estar loco entonces. Debí imaginarme que lo que tenenemos es una cosa diferente, algo de una vez en la vida. ¿Me estás diciendo que todo eso está en mi cabeza y que para ti no es así? ¿Estás completamente seguro que te crees? 

Yo no te amo Edward. Por más que te quiera el amor no es algo que pase en un mes. No sé cómo decirle a lo que sea que siento por ti, pero se siente como la certeza de que tengo que llegar a amarte algún día. Y es verdad, no tengo ninguna razón para estar seguro de eso. Pero aquí estoy ¿No?

Y también estás tú. 

Se te borró un commit Samuel.

Te voy a ser muy sincero, he estado pensando mucho.

Y la verdad es que tu no me conoces, ni yo te conozco a ti.
                        
No tiene sentido que digas todo lo que estás diciendo por alguien que no conoces.
                        
Las palabras se las lleva el viento, y nada te asegura que lo que crees que sientes no sea producto del desconocimiento.
                        
De la idealización.
                        
Podemos intentar negociarlo si quieres. Pero hay mucho de que hablar, mucho detrás.

Las cosas se hacen bien o no se hacen.
                        
Y diciendome que no eres alguien coherente solo lo complica más. Porque entonces no puedo confiar en lo que me dices.
                        
Las líneas 154 y 160 se contradicen, btw.
                        

Está bien.

No se me borró, lo borré.

He estado hablando más rápido de lo que pienso.

Si vamos a negociar, me voy a expresar mejor.

Sobre la contradicción, se puede estar bajo la incorrecta impresión de que se quiere algo, por desconocimiento. Línea 225.

Sin embargo, no pienso que lo que siento por ti sea producto de la idealización. 

Pero si me he equivocado respecto a lo que siento. 

Me lancé muy fuerte. Independientemente de la conexión que tenga contigo, ir de ojos cerrados es irresponsable, y no te corresponde la culpa por eso. 

Fue inmaduro, pero el hecho es que lo hice. Aunque esa sea la causa de la intensidad de lo que siento, no es la causa del sentimiento en sí, eso sigues siendo tú.


Btw, me inspiraste. Compré una libreta y lapiceros de gel del panamericana. Honestamente no sé como le haces para escribir lo que piensas, yo pienso tres veces más rápido de lo que puedo escribir.
Pero está bastante útil para anotar cosas y así, me hacía falta y no sabía


            """)
            st.balloons()
        
        st.subheader("🎯 Sequence Formula")
        st.latex(st.session_state.game_data['formula_latex'])
        
        st.subheader("📊 Full Sequence")
        st.write("**4, 8, 15, 16, 23, 42**")
        st.markdown("*También me prohibieron terminarla, entonces no sé qué signfican.*")
        
        if st.button("🎮 New Game"):
            st.session_state.game_data = generate_sequence()
            st.session_state.current_guess = 5
            st.session_state.show_hint = False
            st.session_state.game_over = False
            st.session_state.gave_up = False
            st.session_state.correct_sequence_guessed = False
            st.rerun()
    

if __name__ == "__main__":
    main()





























