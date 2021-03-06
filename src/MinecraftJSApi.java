import java.io.IOException;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.logging.Logger;

import javax.script.Invocable;
import javax.script.ScriptException;

import net.minecraft.server.MinecraftServer;

public class MinecraftJSApi {
	public static Hashtable<String, ArrayList<Object>> bindings = new Hashtable<String, ArrayList<Object>>();
	
	public static String getPluginName () {
		return ScriptingApi.pluginName;
	}
	
	public static void loadJar (String jar) {
		try {
			ClasspathHacker.addFile(jar);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static String getPluginVersion () {
		return ScriptingApi.pluginVersion;
	}
	
	public static Logger getLog () {
		return ScriptingApi.log;
	}
	
	public static etc getEtc () {
		return etc.getInstance();
	}
	
	public static Server getServer() {
		return etc.getServer();
	}
	
	public static PluginLoader getLoader() {
		return etc.getLoader();
	}
	
	public static MinecraftServer getMCServer() {
		return etc.getMCServer();
	}
	
	public static HitBlox createHitBlox(Object p) {
		return new HitBlox((Player) p);
	}

	public static class PlayerRunnable implements Runnable {
		protected Invocable invoc;
		protected Object obj;
		protected String func;
		
		public PlayerRunnable(Invocable i, Object o, String f) {
			invoc = i;
			obj = o;
			func = f;
		}
	
	    public void run() {
			try {
				invoc.invokeMethod(obj, func, new Object[] {});
			} catch (ScriptException e) {
				e.printStackTrace();
			} catch (NoSuchMethodException e) {
				e.printStackTrace();
			}
		}
	}

	public static PlayerRunnable createRunnable(Object obj) {
		return new MinecraftJSApi.PlayerRunnable(ScriptingApi.invoc.get("js"), obj, "run");
	}
	
	public static Item createItem(int a, int b, int c) {
		return new Item(a,b,c);
	}
	
	public static Item createItem(int a, int b) {
		return new Item(a,b);
	}
	
	public static Item createItem() {
		return new Item();
	}
	
	public static Location createLocation(double a, double b, double c, float x, float y) {
		return new Location(a,b,c,x,y);
	}
	
	public static Location createLocation(double a, double b, double c) {
		return new Location(a,b,c);
	}
	
	public static Location createLocation() {
		return new Location();
	}
	
	public static void broadcast(String message, String group, boolean reverse) {
		for (Player p : etc.getServer().getPlayerList()) {
			if(group.equals("") || (!reverse && p.isInGroup(group))) {
				p.sendMessage(message);
			}
		}		
	}
	
	public static void bind (String key, Object o) {
		if(!bindings.containsKey(key)) {
			bindings.put(key, new ArrayList<Object>());
		}
		
		bindings.get(key).add(o);
	}

	public static Object[] trigger (String key, Object...args) {
		ArrayList<Object> results = new ArrayList<Object>();
		if(bindings.containsKey(key)) {
			for(Object o : bindings.get(key)) {
				try {
					Collection c = ScriptingApi.invoc.values();
					Iterator itr = c.iterator();
					while(itr.hasNext()) {
						Invocable i = (Invocable)itr.next();
						results.add(i.invokeMethod(o, "call", args));
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
		return results.toArray();
	}
	
	public static Object create (String className, Object[] args) throws InstantiationException, IllegalAccessException, ClassNotFoundException, IllegalArgumentException, InvocationTargetException {
		try {
			if(args.length < 1) {
				return Class.forName(className).newInstance();
			} else if(args.length >= 1) {
				Constructor<?>[] c = Class.forName(className).getConstructors();
				for(int i = 0; i < c.length; i++) {
					Constructor<?> thisC = c[i];
					if(thisC.getParameterTypes().length == args.length) {
						boolean stop = false;
						for(int x = 0; x < args.length; x++) {
							if(thisC.getParameterTypes()[x].getCanonicalName() == "int" && args[x].getClass().getCanonicalName() == "java.lang.Double") {
								args[x] = ((Double)args[x]).intValue();
							}
							else if(thisC.getParameterTypes()[x].getCanonicalName() == "int" && args[x].getClass().getCanonicalName() == "java.lang.Integer") {
								args[x] = ((Integer)args[x]).intValue();
							}
							else if(thisC.getParameterTypes()[x].getCanonicalName() != args[x].getClass().getCanonicalName()) {
								stop = true;
							}
						}
						if(stop) {
							continue;
						}
						else {
							return thisC.newInstance(args);
						}
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return new Object();
	}
	
	public static Object getEnum (String className) throws InstantiationException, IllegalAccessException, ClassNotFoundException, IllegalArgumentException, InvocationTargetException {
		return create(className, new Object[] {});
	}
}
