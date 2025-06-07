/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana2.herencia;

/**
 *
 * @author USER
 */
public abstract class Padre {
//atributos
    public String apellido;
    
    //contructor
    Padre(String apellido){
        this.apellido = apellido;
    }
    
    //metodos
    abstract void edad();
}
