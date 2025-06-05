/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana2.herencia;

/**
 *
 * @author USER
 */
public class Hijo extends Padre{
    
    public Hijo(String apellido) {
        super(apellido);
        System.out.println( this.apellido);
    } 

    @Override
    void edad() {
       // calcular edad
       // direcia de edad entre el padre y el hijo
    }
    
    
}
