import { writable } from 'svelte/store';

// 1. Roles del Sistema RBAC (1 = Máxima Autoridad)
export const initialRoles = [
	{ id: 1, nombre: 'Administrador', nivel_jerarquia: 1, descripcion: 'Acceso total y bypass de supervisión sobre todos los módulos' },
	{ id: 2, nombre: 'Coordinador', nivel_jerarquia: 2, descripcion: 'Gestión académica, aprobación de prácticas, convenios y tutores' },
	{ id: 3, nombre: 'Profesor (Tutor Académico)', nivel_jerarquia: 3, descripcion: 'Supervisión directa de prácticas, bitácoras y rúbricas de evaluación' },
	{ id: 4, nombre: 'Estudiante', nivel_jerarquia: 4, descripcion: 'Consulta de prácticas asignadas, carga de documentos y registro de bitácoras' }
];

// 2. Módulos del Sistema
export const initialModulos = [
	{ id: 1, codigo: 'DASHBOARD', nombre: 'Tablero Principal / Métricas', icono: 'bi-speedometer2' },
	{ id: 2, codigo: 'PROGRAMAS', nombre: 'Programas Académicos', icono: 'bi-mortarboard' },
	{ id: 3, codigo: 'EMPRESAS', nombre: 'Empresas Aliadas', icono: 'bi-buildings' },
	{ id: 4, codigo: 'ESTUDIANTES', nombre: 'Estudiantes en Práctica', icono: 'bi-people' },
	{ id: 5, codigo: 'TUTORES', nombre: 'Tutores (Académicos y Empresariales)', icono: 'bi-person-badge' },
	{ id: 6, codigo: 'CONVENIOS', nombre: 'Convenios Institucionales', icono: 'bi-file-earmark-text' },
	{ id: 7, codigo: 'PRACTICAS', nombre: 'Prácticas Profesionales', icono: 'bi-briefcase' },
	{ id: 8, codigo: 'SEGUIMIENTOS', nombre: 'Seguimientos y Bitácoras', icono: 'bi-journal-check' },
	{ id: 9, codigo: 'EVALUACIONES', nombre: 'Evaluaciones Cuantitativas', icono: 'bi-star-half' },
	{ id: 10, codigo: 'DOCUMENTOS', nombre: 'Gestor Documental y ARL', icono: 'bi-folder2-open' },
	{ id: 11, codigo: 'SEGURIDAD', nombre: 'Seguridad y Roles RBAC', icono: 'bi-shield-lock' }
];

// 3. Matriz de Permisos RBAC
export const initialPermisos = [
	{ rol_id: 1, rol: 'Administrador', modulo: 'Programas', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: true },
	{ rol_id: 1, rol: 'Administrador', modulo: 'Empresas', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: true },
	{ rol_id: 1, rol: 'Administrador', modulo: 'Prácticas', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: true },
	{ rol_id: 1, rol: 'Administrador', modulo: 'Seguridad', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: true },
	{ rol_id: 2, rol: 'Coordinador', modulo: 'Programas', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: false },
	{ rol_id: 2, rol: 'Coordinador', modulo: 'Empresas', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: false },
	{ rol_id: 2, rol: 'Coordinador', modulo: 'Prácticas', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: false },
	{ rol_id: 2, rol: 'Coordinador', modulo: 'Seguridad', puede_crear: false, puede_leer: true, puede_actualizar: false, puede_eliminar: false },
	{ rol_id: 3, rol: 'Profesor', modulo: 'Prácticas', puede_crear: false, puede_leer: true, puede_actualizar: false, puede_eliminar: false },
	{ rol_id: 3, rol: 'Profesor', modulo: 'Seguimientos', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: false },
	{ rol_id: 3, rol: 'Profesor', modulo: 'Evaluaciones', puede_crear: true, puede_leer: true, puede_actualizar: true, puede_eliminar: false },
	{ rol_id: 4, rol: 'Estudiante', modulo: 'Prácticas', puede_crear: false, puede_leer: true, puede_actualizar: false, puede_eliminar: false },
	{ rol_id: 4, rol: 'Estudiante', modulo: 'Seguimientos', puede_crear: true, puede_leer: true, puede_actualizar: false, puede_eliminar: false },
	{ rol_id: 4, rol: 'Estudiante', modulo: 'Documentos', puede_crear: true, puede_leer: true, puede_actualizar: false, puede_eliminar: false }
];

// 4. Programas Académicos
export const initialProgramas = [
	{ id: 1, codigo: 'ING-SIS', nombre: 'Ingeniería de Sistemas', facultad: 'Facultad de Ingeniería', nivel: 'Pregrado', creditos: 165, estado: 'Activo' },
	{ id: 2, codigo: 'ADM-EMP', nombre: 'Administración de Empresas', facultad: 'Facultad de Ciencias Económicas', nivel: 'Pregrado', creditos: 150, estado: 'Activo' },
	{ id: 3, codigo: 'DIS-GRA', nombre: 'Diseño Gráfico Digital', facultad: 'Facultad de Artes y Diseño', nivel: 'Pregrado', creditos: 140, estado: 'Activo' },
	{ id: 4, codigo: 'CON-PUB', nombre: 'Contaduría Pública', facultad: 'Facultad de Ciencias Económicas', nivel: 'Pregrado', creditos: 155, estado: 'Activo' },
	{ id: 5, codigo: 'ING-IND', nombre: 'Ingeniería Industrial', facultad: 'Facultad de Ingeniería', nivel: 'Pregrado', creditos: 160, estado: 'Activo' }
];

// 5. Empresas Aliadas
export const initialEmpresas = [
	{ id: 1, nit: '900123456-1', razon_social: 'TechInnovate Solutions S.A.S.', sector: 'Tecnología y Software', contacto: 'Laura Gómez', correo: 'contacto@techinnovate.com', telefono: '601-555-0101', ciudad: 'Bogotá D.C.', estado: 'Activo' },
	{ id: 2, nit: '890900123-5', razon_social: 'Grupo Bancario Andino S.A.', sector: 'Financiero y Banca', contacto: 'Carlos Méndez', correo: 'talento@bancoandino.com.co', telefono: '601-555-0202', ciudad: 'Medellín', estado: 'Activo' },
	{ id: 3, nit: '901456789-3', razon_social: 'BioSalud Laboratorios S.A.', sector: 'Farmacéutico y Salud', contacto: 'Mariana Duarte', correo: 'recursos@biosalud.org', telefono: '602-555-0303', ciudad: 'Cali', estado: 'Activo' },
	{ id: 4, nit: '860002450-8', razon_social: 'Logística Global de Carga Ltda.', sector: 'Transporte y Cadena de Suministro', contacto: 'Roberto Peña', correo: 'rrhh@logisticaglobal.com', telefono: '605-555-0404', ciudad: 'Barranquilla', estado: 'Activo' }
];

// 6. Estudiantes
export const initialEstudiantes = [
	{ id: 1, documento: '1018456789', tipo_doc: 'CC', nombres: 'Mateo Alejandro', apellidos: 'Pérez Suárez', correo: 'mateo.perez@universidad.edu.co', telefono: '3104567890', programa_id: 1, programa: 'Ingeniería de Sistemas', semestre: 9, promedio: 4.3, estado: 'Activo' },
	{ id: 2, documento: '1020789456', tipo_doc: 'CC', nombres: 'Valentina', apellidos: 'Rojas Morales', correo: 'valentina.rojas@universidad.edu.co', telefono: '3117894561', programa_id: 2, programa: 'Administración de Empresas', semestre: 8, promedio: 4.1, estado: 'Activo' },
	{ id: 3, documento: '1032145678', tipo_doc: 'CC', nombres: 'Sebastián', apellidos: 'Castillo Vega', correo: 'sebastian.castillo@universidad.edu.co', telefono: '3151239874', programa_id: 1, programa: 'Ingeniería de Sistemas', semestre: 10, promedio: 4.5, estado: 'Activo' },
	{ id: 4, documento: '1045987123', tipo_doc: 'CC', nombres: 'Camila Andrea', apellidos: 'Herrera Ortiz', correo: 'camila.herrera@universidad.edu.co', telefono: '3209876543', programa_id: 3, programa: 'Diseño Gráfico Digital', semestre: 8, promedio: 4.4, estado: 'Activo' },
	{ id: 5, documento: '1098654321', tipo_doc: 'CC', nombres: 'Daniel Fernando', apellidos: 'Navarro Ruiz', correo: 'daniel.navarro@universidad.edu.co', telefono: '3146549870', programa_id: 4, programa: 'Contaduría Pública', semestre: 9, promedio: 3.9, estado: 'Activo' }
];

// 7. Tutores Académicos
export const initialTutoresAcademicos = [
	{ id: 1, documento: '79845123', nombres: 'Dr. Fernando', apellidos: 'Jaramillo Restrepo', correo: 'fernando.jaramillo@universidad.edu.co', telefono: '3128901234', departamento: 'Ingeniería de Software', especialidad: 'Arquitectura Cloud y DevOps', estado: 'Activo' },
	{ id: 2, documento: '52678901', nombres: 'Dra. Claudia Patricia', apellidos: 'Maldonado Gómez', correo: 'claudia.maldonado@universidad.edu.co', telefono: '3167890123', departamento: 'Gestión Organizacional', especialidad: 'Estrategia Empresarial', estado: 'Activo' },
	{ id: 3, documento: '80123456', nombres: 'Mg. Javier Enrique', apellidos: 'Torres Cárdenas', correo: 'javier.torres@universidad.edu.co', telefono: '3189012345', departamento: 'Artes y Tecnologías Digitales', especialidad: 'Diseño UX/UI e Interacción', estado: 'Activo' }
];

// 8. Tutores Empresariales
export const initialTutoresEmpresariales = [
	{ id: 1, documento: '19876543', empresa_id: 1, empresa: 'TechInnovate Solutions S.A.S.', nombres: 'Ing. Andrea', apellidos: 'Salazar Marín', cargo: 'Tech Lead / Gerente de Desarrollo', correo: 'asalazar@techinnovate.com', telefono: '3001234567', estado: 'Activo' },
	{ id: 2, documento: '80456123', empresa_id: 2, empresa: 'Grupo Bancario Andino S.A.', nombres: 'Lic. Guillermo', apellidos: 'Ospina Bravo', cargo: 'Director de Riesgos Financieros', correo: 'gospina@bancoandino.com.co', telefono: '3012345678', estado: 'Activo' },
	{ id: 3, documento: '51987654', empresa_id: 3, empresa: 'BioSalud Laboratorios S.A.', nombres: 'Q.F. Mónica', apellidos: 'Londoño Gil', cargo: 'Coordinadora de Calidad y Procesos', correo: 'mlondono@biosalud.org', telefono: '3023456789', estado: 'Activo' }
];

// 9. Convenios
export const initialConvenios = [
	{ id: 1, codigo: 'CONV-2026-001', empresa_id: 1, empresa: 'TechInnovate Solutions S.A.S.', tipo: 'Convenio Marco de Cooperación', fecha_inicio: '2026-01-15', fecha_fin: '2027-12-31', cupos_totales: 8, cupos_disponibles: 5, estado: 'Vigente' },
	{ id: 2, codigo: 'CONV-2026-002', empresa_id: 2, empresa: 'Grupo Bancario Andino S.A.', tipo: 'Convenio Específico de Prácticas', fecha_inicio: '2026-02-01', fecha_fin: '2026-12-15', cupos_totales: 5, cupos_disponibles: 2, estado: 'Vigente' },
	{ id: 3, codigo: 'CONV-2025-018', empresa_id: 3, empresa: 'BioSalud Laboratorios S.A.', tipo: 'Convenio Marco de Investigación y Práctica', fecha_inicio: '2025-08-01', fecha_fin: '2026-07-31', cupos_totales: 4, cupos_disponibles: 1, estado: 'Próximo a Vencer' }
];

// 10. Prácticas Profesionales (Entidad Central)
export const initialPracticas = [
	{
		id: 1,
		estudiante_id: 1,
		estudiante_nombre: 'Mateo Alejandro Pérez Suárez',
		programa: 'Ingeniería de Sistemas',
		empresa_id: 1,
		empresa_nombre: 'TechInnovate Solutions S.A.S.',
		convenio_codigo: 'CONV-2026-001',
		tutor_academico: 'Dr. Fernando Jaramillo Restrepo',
		tutor_empresarial: 'Ing. Andrea Salazar Marín',
		cargo_estudiante: 'Desarrollador Full Stack Junior',
		fecha_inicio: '2026-02-01',
		fecha_fin: '2026-07-31',
		horas_totales: 640,
		horas_completadas: 320,
		estado: 'En Proceso',
		modalidad: 'Híbrida'
	},
	{
		id: 2,
		estudiante_id: 2,
		estudiante_nombre: 'Valentina Rojas Morales',
		programa: 'Administración de Empresas',
		empresa_id: 2,
		empresa_nombre: 'Grupo Bancario Andino S.A.',
		convenio_codigo: 'CONV-2026-002',
		tutor_academico: 'Dra. Claudia Patricia Maldonado Gómez',
		tutor_empresarial: 'Lic. Guillermo Ospina Bravo',
		cargo_estudiante: 'Analista de Operaciones y Procesos',
		fecha_inicio: '2026-02-15',
		fecha_fin: '2026-08-15',
		horas_totales: 640,
		horas_completadas: 280,
		estado: 'En Proceso',
		modalidad: 'Presencial'
	},
	{
		id: 3,
		estudiante_id: 3,
		estudiante_nombre: 'Sebastián Castillo Vega',
		programa: 'Ingeniería de Sistemas',
		empresa_id: 1,
		empresa_nombre: 'TechInnovate Solutions S.A.S.',
		convenio_codigo: 'CONV-2026-001',
		tutor_academico: 'Dr. Fernando Jaramillo Restrepo',
		tutor_empresarial: 'Ing. Andrea Salazar Marín',
		cargo_estudiante: 'Ingeniero QA y Pruebas Automatizadas',
		fecha_inicio: '2026-01-20',
		fecha_fin: '2026-06-30',
		horas_totales: 640,
		horas_completadas: 410,
		estado: 'En Proceso',
		modalidad: 'Remota'
	},
	{
		id: 4,
		estudiante_id: 4,
		estudiante_nombre: 'Camila Andrea Herrera Ortiz',
		programa: 'Diseño Gráfico Digital',
		empresa_id: 1,
		empresa_nombre: 'TechInnovate Solutions S.A.S.',
		convenio_codigo: 'CONV-2026-001',
		tutor_academico: 'Mg. Javier Enrique Torres Cárdenas',
		tutor_empresarial: 'Ing. Andrea Salazar Marín',
		cargo_estudiante: 'Diseñadora UI/UX Junior',
		fecha_inicio: '2026-03-01',
		fecha_fin: '2026-08-31',
		horas_totales: 640,
		horas_completadas: 160,
		estado: 'Pendiente Aprobación',
		modalidad: 'Híbrida'
	}
];

// 11. Seguimientos / Bitácoras
export const initialSeguimientos = [
	{ id: 1, practica_id: 1, estudiante_nombre: 'Mateo Alejandro Pérez', numero_semana: 8, fecha_registro: '2026-03-27', horas_reportadas: 40, actividad: 'Diseño e implementación de microservicios REST con FastAPI y validación Pydantic', observaciones: 'Excelente progreso, código limpio y buenas prácticas de git', estado: 'Aprobado' },
	{ id: 2, practica_id: 1, estudiante_nombre: 'Mateo Alejandro Pérez', numero_semana: 9, fecha_registro: '2026-04-03', horas_reportadas: 40, actividad: 'Integración de base de datos PostgreSQL en la nube Neon con triggers de auditoría', observaciones: 'Cumplimiento adecuado de los lineamientos del equipo', estado: 'Aprobado' },
	{ id: 3, practica_id: 2, estudiante_nombre: 'Valentina Rojas Morales', numero_semana: 7, fecha_registro: '2026-03-30', horas_reportadas: 38, actividad: 'Levantamiento de indicadores de tiempo de ciclo para trámites de crédito bancario', observaciones: 'Entrega oportuna de matriz de riesgos en formato institucional', estado: 'Aprobado' },
	{ id: 4, practica_id: 3, estudiante_nombre: 'Sebastián Castillo Vega', numero_semana: 10, fecha_registro: '2026-04-05', horas_reportadas: 40, actividad: 'Ejecución de pruebas automatizadas E2E y reporte de cobertura de código', observaciones: 'Pendiente revisión de métricas por parte del tutor empresarial', estado: 'En Revisión' }
];

// 12. Evaluaciones Cuantitativas
export const initialEvaluaciones = [
	{ id: 1, practica_id: 1, estudiante_nombre: 'Mateo Alejandro Pérez', tipo: 'Evaluación de Medio Término', competencia_tecnica: 4.8, competencia_actitudinal: 5.0, puntualidad: 4.7, calificacion_final: 4.8, observaciones: 'Demuestra alto rigor técnico, autonomía y proactividad en el equipo.', evaluador: 'Ing. Andrea Salazar (Tutor Empresarial)', fecha: '2026-03-20', estado: 'Aprobada' },
	{ id: 2, practica_id: 2, estudiante_nombre: 'Valentina Rojas Morales', tipo: 'Evaluación de Medio Término', competencia_tecnica: 4.3, competencia_actitudinal: 4.6, puntualidad: 4.5, calificacion_final: 4.5, observaciones: 'Excelente capacidad de análisis, liderazgo y trabajo en equipo.', evaluador: 'Lic. Guillermo Ospina (Tutor Empresarial)', fecha: '2026-03-25', estado: 'Aprobada' },
	{ id: 3, practica_id: 3, estudiante_nombre: 'Sebastián Castillo Vega', tipo: 'Evaluación de Medio Término', competencia_tecnica: 4.6, competencia_actitudinal: 4.4, puntualidad: 4.8, calificacion_final: 4.6, observaciones: 'Soluciones estructuradas y meticulosa documentación de pruebas.', evaluador: 'Ing. Andrea Salazar (Tutor Empresarial)', fecha: '2026-03-22', estado: 'Aprobada' }
];

// 13. Documentos y Soportes
export const initialDocumentos = [
	{ id: 1, practica_id: 1, estudiante_nombre: 'Mateo Alejandro Pérez', tipo_documento: 'Carta de Aceptación Empresarial', archivo_nombre: 'Carta_Aceptacion_MateoPerez.pdf', fecha_subida: '2026-01-25', estado: 'Aprobado', observaciones: 'Firmada y sellada por RRHH TechInnovate' },
	{ id: 2, practica_id: 1, estudiante_nombre: 'Mateo Alejandro Pérez', tipo_documento: 'Afiliación ARL Vigente', archivo_nombre: 'Certificado_ARL_Sura_2026.pdf', fecha_subida: '2026-01-28', estado: 'Aprobado', observaciones: 'Riesgo I verificado con cobertura total' },
	{ id: 3, practica_id: 1, estudiante_nombre: 'Mateo Alejandro Pérez', tipo_documento: 'Plan de Trabajo Concertado', archivo_nombre: 'Plan_Trabajo_Firmado_Mateo.pdf', fecha_subida: '2026-02-05', estado: 'Aprobado', observaciones: 'Aprobado por el tutor académico' },
	{ id: 4, practica_id: 2, estudiante_nombre: 'Valentina Rojas Morales', tipo_documento: 'Afiliación ARL Vigente', archivo_nombre: 'ARL_Bolivar_ValentinaRojas.pdf', fecha_subida: '2026-02-10', estado: 'Aprobado', observaciones: 'Vigente hasta fin de prácticas' },
	{ id: 5, practica_id: 4, estudiante_nombre: 'Camila Andrea Herrera', tipo_documento: 'Carta de Aceptación Empresarial', archivo_nombre: 'Carta_Tech_CamilaHerrera.pdf', fecha_subida: '2026-02-28', estado: 'Pendiente Revisión', observaciones: 'Falta firma del decano de facultad' }
];

// Stores Reactivos de Svelte para permitir interacción en vivo en la aplicación
export const programasStore = writable(initialProgramas);
export const empresasStore = writable(initialEmpresas);
export const estudiantesStore = writable(initialEstudiantes);
export const tutoresAcademicosStore = writable(initialTutoresAcademicos);
export const tutoresEmpresarialesStore = writable(initialTutoresEmpresariales);
export const conveniosStore = writable(initialConvenios);
export const practicasStore = writable(initialPracticas);
export const seguimientosStore = writable(initialSeguimientos);
export const evaluacionesStore = writable(initialEvaluaciones);
export const documentosStore = writable(initialDocumentos);

// Rol activo actual en la interfaz (permite simular la experiencia como Admin, Coord, Docente o Alumno)
export const rolActivoStore = writable({
	id: 1,
	nombre: 'Administrador',
	nivel_jerarquia: 1,
	usuario: 'Ivan Carrillo (Admin Central)',
	icono: 'bi-shield-check'
});
