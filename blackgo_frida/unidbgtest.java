public class BcfTest {
    private final AndroidEmulator emulator;
    private final VM vm;
    private final DvmClass mainActivityDvm;

    public static void main(String[] args) {
        BcfTest bcfTest = new BcfTest();
        bcfTest.call_calckey();
    }

    private BcfTest() {
        emulator = AndroidEmulatorBuilder
                .for64Bit()
                .build();
        Memory memory = emulator.getMemory();
        LibraryResolver resolver = new AndroidResolver(23);
        memory.setLibraryResolver(resolver);
        vm = emulator.createDalvikVM(null);
        vm.setVerbose(false);
        mainActivityDvm = vm.resolveClass("com/example/ollvmdemo2/MainActivity");
        DalvikModule dm = vm.loadLibrary(new File("unidbg-android/src/test/resources/example_binaries/ollvm_bcf/libnative-lib.so"), false);
        dm.callJNI_OnLoad(emulator);
    }

    //主动调用目标函数
    private void call_calckey() {
        //调用一个返回值为object的静态的jni函数
        StringObject res = mainActivityDvm.callStaticJniMethodObject(emulator, "stringFromJNI()Ljava/lang/String;");
        System.out.println(res.toString());
    }
}
