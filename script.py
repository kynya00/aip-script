# version 2.0
# Change: new zastava for win7x64. Слияние всех веток в одну.  
import os
import platform
import subprocess
import shutil
#import winshell
import sys
import traceback

try:
    plat = platform.machine() # определяю платформу архитектуры
    path_to_dir = "C:/Program Files/Crypto Pro/CSP" # можно сделать интереснее, но лень
    path_to_documents = os.path.join(os.environ['USERPROFILE'], "Documents")
    if not os.path.exists(path_to_documents):
        os.mkdir(path_to_documents)
    path_to_logs_python = os.path.join(os.environ['USERPROFILE'], "Documents/csp_zast_logs/errors_log_file.log")
    path_to_logs = os.path.join(os.environ['USERPROFILE'], "Documents/csp_zast_logs") # путь к логам установки
    path_to_zastava_client = "C:/Program Files/ELVIS+/ZASTAVA Client/vpnconfig.exe" # путь к впн конфигу
    path_to_zastava_client_plg = "C:/Program Files/ELVIS+/ZASTAVA Client/plg_ctl.exe" # путь к plg_ctl
    if not os.path.exists(path_to_documents):
        os.mkdir(path_to_documents)
    if not os.path.exists(path_to_logs): # хотфикс если уже создана папка логирования установок
        os.mkdir(path_to_logs)
    file_logs = open(path_to_logs_python, "a")
    file_logs.close
    path_to_logs_no_end = path_to_logs[3:] # хотфикс path.join (при использовании ниже сборки строки ?, ругается на лишние сплешы порезал их)
    workdir = os.getcwd() # рабочая папка
    workdir_train = workdir[3:] #мелкий хотфикс для join path, у него есть своя особенность (гугол)
    path_to_rutoken = "\"C:\Windows\System32\Aktiv Co\"" # аля путь до токена
    my_os = "systeminfo | findstr /C:\"Server\"" # хотфикс на проверку серверной шиндовс или клиентская
    my_os_name = subprocess.run(my_os, shell=True, capture_output=True) # переменная которая хранит вывод
    aktiv_co = "reg query HKLM\SOFTWARE | findstr Aktiv"
    aktiv_co_name = subprocess.run(aktiv_co, shell=True, capture_output=True) # переменная которая хранит вывод реестра на наличие рутокена в системе (костыль)

    #---------------БЛОГ ПРЕДУСТАНОВКИ ПОЛИТИК И СЕРТИФИКАТОВ В ЗАСТАВУ--------------
    def zastava_configuration():
        print("Добавление корневых сертификатов Zastava Client...")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + "cert pin $PIN"
        err_vpn_cert_1 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # установка корневого
        if err_vpn_cert_1.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_1.returncode, "Вывод:", err_vpn_cert_1.stderr, err_vpn_cert_1.stdout,"Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_2 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # установка корневого
        if err_vpn_cert_2.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_2.returncode, "Вывод:", err_vpn_cert_2.stderr, err_vpn_cert_2.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_3 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # установка корневого
        if err_vpn_cert_3.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_3.returncode, "Вывод:", err_vpn_cert_3.stderr, err_vpn_cert_3.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_4 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, stdout=False) # установка корневого
        if err_vpn_cert_4.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_4.returncode, "Вывод:", err_vpn_cert_4.stderr, err_vpn_cert_4.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_5 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, stdout=False) # установка корневого
        if err_vpn_cert_5.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_5.returncode, "Вывод:", err_vpn_cert_5.stderr, err_vpn_cert_5.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_6 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, stdout=False) # установка корневого
        if err_vpn_cert_6.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_6.returncode, "Вывод:", err_vpn_cert_6.stderr, err_vpn_cert_6.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_7 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, stdout=False) # установка корневого
        if err_vpn_cert_7.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_7.returncode, "Вывод:", err_vpn_cert_7.stderr, err_vpn_cert_7.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_8 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, stdout=False) # установка корневого
        if err_vpn_cert_8.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_8.returncode, "Вывод:", err_vpn_cert_8.stderr, err_vpn_cert_8.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -add cert C:/" + workdir_train + ""cert pin $PIN""
        err_vpn_cert_9 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, stdout=False) # установка корневого
        if err_vpn_cert_9.returncode != 0:
            print("Во время конфигурирования Zastava Client произошла ошибка (cer): ", err_vpn_cert_9.returncode, "Вывод:", err_vpn_cert_9.stderr, err_vpn_cert_9.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Сертификат cer успешно добавлен.")
        if my_os_name.returncode == 1:
            path_to_zastava_install_commands = '\"' + path_to_zastava_client + "\""  + " -a lsp user pmp any DN $SERVER_IP"
            err_vpn_political = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # установка юзерской политики
            if err_vpn_political.returncode != 0:
                print("Во время конфигурирования Zastava Client произошла ошибка (user-politics): ", err_vpn_political.returncode, "Вывод:", err_vpn_political.stderr, "Обратитесь в техническую поддержку.")
                os.system("pause")
                sys.exit()
            else:
                print("Конфигурация политики Zastava Client завершена успешно.")
        else:
            err_vpn_political = "Для операционной системы Windows \"Server\" политику необходимо сконфигурировать вручную по инструкции."
            print("Для операционной системы Windows \"Server\" политику необходимо сконфигурировать вручную по инструкции.")

        path_to_zastava_install_commands = '\"' + path_to_zastava_client_plg + "\""  + " -r cp_plg_gost_user"
        err_vpn_del = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # удаление криптобиблиотек
        if err_vpn_del.returncode != 0:
            print("Во время конфигурирования произошла ошибка (cp_plg_gost_user): ", err_vpn_del.returncode, "Вывод:", err_vpn_del.stderr, "Обратитесь в техническую поддержку.")
            sys.exit()
        else:
            print("Криптобиблиотека cp_plg_gost_user успешно удалена.")
        path_to_zastava_install_commands = '\"' + path_to_zastava_client_plg + "\""  + " -r crypto_cpro_user"
        err_vpn_del_2 = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # удаление криптобиблиотек 
        if err_vpn_del_2.returncode != 0:
            print("Во время конфигурирования произошла ошибка (crypto_cpro_user): ", err_vpn_del_2.returncode, "Вывод:", err_vpn_del_2.stderr, "Обратитесь в техническую поддержку.")
            sys.exit()
        else:
            print("Криптобиблиотека crypto_cpro_user успешно удалена.")
        path_to_zastava_install_commands = "\"C:/Program Files/ELVIS+/ZASTAVA Client/plg_ctl.exe\" -i \"C:/Program Files/ELVIS+/ZASTAVA Client/cp_plg_gost.cfg\" -d \"C:/Program Files/ELVIS+/ZASTAVA Client/cp_plg_gost.dll\""
        err_vpn_inst = subprocess.run(path_to_zastava_install_commands, shell=True, text=True, capture_output=True) # установка криптобиблиотеки
        if err_vpn_inst.returncode != 0:
            print("Во время конфигурирования установки политики произошла ошибка: ", err_vpn_inst.returncode, "Вывод:", err_vpn_inst.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Криптобиблиотека cp_plg_gost_user успешно установлена.")
        file = open(os.path.join(path_to_logs, "file_logs_cmd.txt"), "a") # logs for cmd and any errors
        file.write(str(err_vpn_cert_1) + '\n')
        file.write(str(err_vpn_cert_2) + '\n')
        file.write(str(err_vpn_cert_3) + '\n')
        file.write(str(err_vpn_cert_4) + '\n')
        file.write(str(err_vpn_cert_5) + '\n')
        file.write(str(err_vpn_cert_6) + '\n')
        file.write(str(err_vpn_cert_7) + '\n')
        file.write(str(err_vpn_cert_8) + '\n')
        file.write(str(err_vpn_cert_9) + '\n')
        file.write(str(err_vpn_political) + '\n')
        file.write(str(err_vpn_del) + '\n')
        file.write(str(err_vpn_del_2) + '\n')
        file.write(str(err_vpn_inst) + '\n')
        file.close()
        print("Конфигурация Zastava Client завершена!")
    #-----------------------------------------------------------------

    #--------------БЛОК УСТАНОВКИ RUTOKEN----------------------------
    if aktiv_co_name.returncode != 0: # проверка на папку, если нет то установи
        print("Установка RuToken...")
        file_dir_rutoken = os.path.join(workdir, "rtDrivers.exe /install /norestart /quiet /log \"", path_to_logs_no_end, "log-install-RuToken.txt\"")
        err_rutoken = subprocess.run(file_dir_rutoken, shell=True, check=True, text=True, capture_output=True)
        if err_rutoken.returncode != 0:
            print("Во время установки RuToken произошла ошибка: ", err_rutoken.returncode, "Вывод:", err_rutoken.stdout, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else:
            print("Установка RuToken завершена.")
        file = open(os.path.join(path_to_logs, "file_logs_cmd.txt"), "a") # logs for cmd and any errors
        file.write(str(err_rutoken)+ '\n')
        file.close()
    else:
        print("RuToken уже установлен.")
    #----------------------------------------------------------------

    #--------------БЛОК УСТАНОВКИ CSPCSPC----------------------------
    if os.path.exists(path_to_dir) == False and (my_os_name.returncode == 0):
        print("Установка Crypto Pro...") # установка CryptoPro для серверной части (без PIDKEY)
        file_dir_csp = os.path.join(workdir, "csp_usefull.exe -silent -noreboot -nodlg -lang rus -args \"/passive /quiet /L*v \"", path_to_logs_no_end, "log-install-cryptopro.txt\"")
        err_csp = subprocess.run(file_dir_csp, shell=True, check=True, text=True, capture_output=True)
        file = open(os.path.join(path_to_logs, "file_logs_cmd.txt"), "a") # logs for cmd and any errors
        file.write(str(err_csp)+ '\n')
        file.close()
        if err_csp.returncode != 0:
            print("Во время установки CryptoPro произошла ошибка: ", err_csp.returncode, "Вывод:", err_csp.stderr, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else: 
            print("Установка Crypto Pro завершена!")
    elif os.path.exists(path_to_dir) == False:
        print("Установка Crypto Pro...") #установка CryptoPro для клиентской части (c PIDKEY)
        file_dir_csp = os.path.join(workdir, "csp_usefull.exe -silent -noreboot -nodlg -lang rus -args \"PIDKEY=? /passive /quiet /L*v \"", path_to_logs_no_end, "log-install-cryptopro.txt\"")
        err_csp = subprocess.run(file_dir_csp, shell=True, check=True, text=True, capture_output=True)
        file = open(os.path.join(path_to_logs, "file_logs_cmd.txt"), "a") # logs for cmd and any errors
        file.write(str(err_csp)+ '\n')
        file.close()
        if err_csp.returncode != 0:
            print("Во время установки CryptoPro произошла ошибка:", err_csp.returncode, "Вывод:", err_csp.stderr, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else: 
            print("Установка Crypto Pro завершена!")
    else:
        print("CryptoPro уже установлен.")
    #-----------------------------------------------------------------

    #--------------БЛОК УСТАНОВКИ VC_RED:ZASTAVA---------------
    # установка zastava + vcred + nx для 64бит
    if plat == 'AMD64':
        file_dir_exe = os.path.join(workdir, "vcred/vc_redist.x64.exe /norestart /quiet /L \"", path_to_logs_no_end, "log-vc-regit.txt\"") # установка vc-red
        err_vcred = subprocess.run(file_dir_exe, shell=True, capture_output=True)
        print("Установка Zastava Client...")
        file_dir_zastava = os.path.join(workdir, "zastava64/client.msi /quiet /norestart /qn /l* \"", path_to_logs_no_end, "log-install-zastava.txt\"") # установка заставы
        err_zastava = subprocess.run(file_dir_zastava, shell=True, check=True, text=True, capture_output=True)
        if err_zastava.returncode != 0:
            print("Во время установки Zastava Client произошла ошибка: ", err_zastava.returncode, "Вывод:", err_zastava.stderr, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else: 
            print("Установка Zastava Client завершена!")
        zastava_configuration()
        file = open(os.path.join(path_to_logs, "file_logs_cmd.txt"), "a") # logs for cmd and any errors
        file.write(str(err_vcred)+ '\n')
        file.write(str(err_zastava)+ '\n')
        file.close()
    # установка zastava + vcred для 32бит
    else:
        file_dir_exe = os.path.join(workdir, "vcred/vc_redist.x86.exe /norestart /quiet /L \"", path_to_logs_no_end, "log-vc-regit.txt\"")  # установка vc-red
        err_vcred = subprocess.run(file_dir_exe, shell=True, text=True, capture_output=True)
        print("Установка Zastava Client...")
        file_dir_zastava = os.path.join(workdir, "zastava32/client.exe /quiet /norestart /qn /l* \"", path_to_logs_no_end, "log-install-zastava.txt\"")
        err_zastava = subprocess.run(file_dir_zastava, shell=True, check=True, text=True, capture_output=True)  # установка заставы
        if err_zastava.returncode != 0:
            print("Во время установки Zastava Client произошла ошибка", err_zastava.returncode, err_zastava.stderr, "Обратитесь в техническую поддержку.")
            os.system("pause")
            sys.exit()
        else: 
            print("Установка Zastava Client завершена!")
        zastava_configuration()
        file = open(os.path.join(path_to_logs, "file_logs_cmd.txt"), "a") # logs for cmd and any errors
        file.write(str(err_vcred) + '\n')
        file.write(str(err_zastava) + '\n')
        file.close()
    #----------------------------------------------------------------
    print("Установка завершена!")
    os.system("pause")
except Exception as e:
    err_2 = traceback.format_exc()
    file_open = open(path_to_logs_python, 'a')
    file_open.write(str(err_2))
    file_open.close()
    print("_____________________________________________________________________________")
    print("Во время автоинсталяции произошла ошибка, обратитесь в техническую поддержку.")
    os.system("pause")
