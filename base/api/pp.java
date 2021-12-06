class PatientProblems extends Thread {
	String[] arr;
	HospitalThreads x;

	public PatientProblems(String arr[], HospitalThreads x) {
		this.arr = arr;
		this.x = x;
	}
	public void run() {
		for (String patientProblems : arr) {
			x.PrintPatientProblems(patientProblems);
		}
	}
}
class Treatment extends Thread {
	String[] arr;
	HospitalThreads x;

	public Treatment(String arr[], HospitalThreads x) {
		this.arr = arr;
		this.x = x;
	}
	public void run() {
		for (String treatment : arr) {
			x.PrintTreatment(treatment);
		}
	}
}
class HospitalThreads {
	boolean PatientProblemsActive = false;
	synchronized void PrintPatientProblems(String z) {
		while (PatientProblemsActive) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println(Thread.currentThread().getName() + " : " + z);
		PatientProblemsActive = true;
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		notify();
	}
	synchronized void PrintTreatment(String z) {
		while (!PatientProblemsActive) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println(Thread.currentThread().getName() + " : " + z);
		System.out.println();
		PatientProblemsActive = false;
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		notify();
	}
}
public class Main {
	public static void main(String[] args) {
		String[] PatientProblemsArray = {
			"What is multithreaded programming?",
			"What is true about time slicing?",
			"Which of the following will ensure the thread will be in runningstate?",
			"Which of the following is a correct constructor for thread?",
			"Which of the following stops execution of a thread?"
		};
		String[] TreatmentArray = {
			"It's a process in which two or more parts of same process run simultaneously",
			"Time slicing is the process to divide the available CPU time toavailable runnable thread",
			"wait()",
			"Thread(Runnable a, String str)",
			"Calling notify() method on an object"
		};
		HospitalThreads x = new HospitalThreads();
		PatientProblems a = new PatientProblems(PatientProblemsArray, x);
		a.setName("PatientProblems Thread");
		Treatment b = new Treatment(TreatmentArray, x);
		b.setName("Treatment Thread");
		a.start();
		b.start();
	}
}
